import { useState, useCallback, useRef } from 'react'

/**
 * ComfyDebugger — A dedicated panel for testing ComfyUI connectivity,
 * workflow injection, and image generation in isolation.
 */
export default function ComfyDebugger() {
  const [comfyUrl, setComfyUrl] = useState('http://localhost:8188')
  const [workflowJson, setWorkflowJson] = useState('')
  const [testPrompt, setTestPrompt] = useState('A professional portrait of a character, photorealistic, 8k')
  const [nodeId, setNodeId] = useState('')
  
  const [status, setStatus] = useState('idle') // idle | testing | generating | done | error
  const [logs, setLogs] = useState([])
  const [promptId, setPromptId] = useState('')
  const [imageUrl, setImageUrl] = useState('')
  const [error, setError] = useState(null)

  const log = (msg) => setLogs(prev => [...prev.slice(-19), `[${new Date().toLocaleTimeString()}] ${msg}`])

  const handleTestConnection = async () => {
    setStatus('testing')
    setError(null)
    log(`Testing connection to ${comfyUrl}...`)
    try {
      const res = await fetch('/api/comfyui/test', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ comfy_url: comfyUrl })
      })
      const data = await res.json()
      if (!res.ok) throw new Error(data.detail || 'Connection failed')
      log('Connection OK! System stats received.')
      setStatus('idle')
    } catch (err) {
      log(`Error: ${err.message}`)
      setError(err.message)
      setStatus('error')
    }
  }

  const handleFileUpload = (e) => {
    const file = e.target.files[0]
    if (!file) return
    const reader = new FileReader()
    reader.onload = (event) => {
      try {
        const json = JSON.parse(event.target.result)
        setWorkflowJson(JSON.stringify(json, null, 2))
        log(`Loaded workflow: ${file.name}`)
      } catch (err) {
        log('Error parsing JSON file.')
        setError('Invalid JSON file')
      }
    }
    reader.readAsText(file)
  }

  const handleGenerate = async () => {
    if (!workflowJson) {
      setError('Please load or paste a workflow JSON first.')
      return
    }

    setStatus('generating')
    setLogs([])
    setImageUrl('')
    setPromptId('')
    setError(null)
    log('Starting generation stream...')

    try {
      const res = await fetch('/api/comfyui/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          comfy_url: comfyUrl,
          workflow_json: workflowJson,
          prompt_text: testPrompt,
          node_id: nodeId || null
        })
      })

      if (!res.ok) {
        const errText = await res.text()
        throw new Error(errText)
      }

      const reader = res.body.getReader()
      const decoder = new TextDecoder()

      while (true) {
        const { value, done } = await reader.read()
        if (done) break

        const chunk = decoder.decode(value)
        const lines = chunk.split('\n')

        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const data = JSON.parse(line.slice(6))
              log(`${data.status.toUpperCase()}: ${data.message}`)
              
              if (data.prompt_id) setPromptId(data.prompt_id)
              
              if (data.status === 'done') {
                setImageUrl(`/api/comfyui/image/${data.prompt_id}`)
                setStatus('done')
              } else if (data.status === 'error') {
                setError(data.message)
                setStatus('error')
              }
            } catch (e) {
              // chunking might split a json line, skip silently
            }
          }
        }
      }
    } catch (err) {
      log(`Stream Error: ${err.message}`)
      setError(err.message)
      setStatus('error')
    }
  }

  return (
    <div className="comfy-debugger animate-in">
      <div className="glass-card">
        <div className="section-header">
          <div className="section-number">DEBUG</div>
          <div>
            <h2>ComfyUI Diagnostic Tool</h2>
            <p className="section-subtitle">Test connectivity, workflow injection, and generation logic</p>
          </div>
          <div className="comfy-logo">🛠️</div>
        </div>

        <div className="form-group">
          <label>ComfyUI Server URL</label>
          <div className="comfy-url-row">
            <input 
              type="text" 
              className="input flex-1" 
              value={comfyUrl} 
              onChange={e => setComfyUrl(e.target.value)}
              placeholder="http://localhost:8188"
            />
            <button 
              className={`btn btn-secondary comfy-test-btn ${status === 'testing' ? 'loading' : ''}`}
              onClick={handleTestConnection}
              disabled={status === 'testing' || status === 'generating'}
            >
              Test Connection
            </button>
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label>API Workflow (JSON)</label>
            <textarea 
              className="textarea" 
              value={workflowJson}
              onChange={e => setWorkflowJson(e.target.value)}
              placeholder="Paste ComfyUI API JSON here..."
            />
            <input 
              type="file" 
              accept=".json" 
              onChange={handleFileUpload} 
              id="debug-file-upload" 
              hidden 
            />
            <button 
              className="btn btn-secondary" 
              style={{marginTop: '8px'}}
              onClick={() => document.getElementById('debug-file-upload').click()}
            >
              📁 Load File
            </button>
          </div>
          
          <div className="form-group">
            <label>Test Prompt & ID</label>
            <textarea 
              className="textarea" 
              style={{minHeight: '80px'}}
              value={testPrompt}
              onChange={e => setTestPrompt(e.target.value)}
            />
            <div style={{marginTop: '12px'}}>
              <label>Target Node ID <span className="label-hint">(Optional)</span></label>
              <input 
                type="text" 
                className="input" 
                value={nodeId}
                onChange={e => setNodeId(e.target.value)}
                placeholder="e.g. 6"
              />
            </div>
            
            <button 
              className="btn btn-primary comfy-gen-btn"
              style={{marginTop: '24px', width: '100%'}}
              onClick={handleGenerate}
              disabled={status === 'generating' || !workflowJson}
            >
              {status === 'generating' ? 'Generating...' : '🚀 Execute generation'}
            </button>
          </div>
        </div>

        {error && (
            <div className="error-badge" style={{width: '100%', marginTop: '12px'}}>
                <span>⚠️ {error}</span>
            </div>
        )}

        <div className="debug-logs" style={{
            marginTop: '24px',
            background: 'rgba(0,0,0,0.4)',
            borderRadius: '12px',
            padding: '16px',
            border: '1px solid var(--border)',
            fontFamily: 'monospace',
            fontSize: '0.8rem',
            minHeight: '120px'
        }}>
            <div style={{color: 'var(--text-muted)', marginBottom: '8px', textTransform: 'uppercase', fontSize: '0.7rem'}}>Live Debug Logs</div>
            {logs.length === 0 && <div style={{color: 'var(--text-faint)'}}>No activity yet...</div>}
            {logs.map((l, i) => (
                <div key={i} style={{marginBottom: '4px', color: l.includes('ERROR') ? 'var(--error)' : 'var(--text)'}}>{l}</div>
            ))}
        </div>

        {imageUrl && (
            <div className="comfy-image-frame animate-in" style={{marginTop: '24px'}}>
                <div className="comfy-image-header">
                    <span>Generated Test Result</span>
                    <span className="comfy-prompt-id">{promptId.slice(0,8)}...</span>
                </div>
                <img 
                    src={imageUrl} 
                    alt="Debug Result" 
                    className="comfy-image" 
                    style={{opacity: 1}}
                />
                <div style={{padding: '12px', textAlign: 'center'}}>
                    <a href={imageUrl} target="_blank" rel="noreferrer" className="btn-copy" style={{textDecoration: 'none'}}>Open in new tab</a>
                </div>
            </div>
        )}
      </div>
    </div>
  )
}
