import { useState, useCallback, useRef } from 'react'
import { Loader } from './Loader'

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

  const [sysResults, setSysResults] = useState(null)
  const [sysLoading, setSysLoading] = useState(false)

  const handleSystemTest = async () => {
    setSysLoading(true)
    log('Running system-wide diagnostic tests...')
    try {
      const res = await fetch('/api/debug/system-test')
      const data = await res.json()
      setSysResults(data)
      log('System tests complete.')
    } catch (err) {
      log(`System Test Error: ${err.message}`)
      setError(err.message)
    } finally {
      setSysLoading(false)
    }
  }

  const getStatusColor = (status) => {
    switch (status) {
      case 'ok': return 'var(--success)';
      case 'warning': return 'var(--gold)';
      case 'error': return 'var(--error)';
      default: return 'var(--text-faint)';
    }
  }

  return (
    <div className="comfy-debugger animate-in">
      <div className="glass-card">
        <div className="section-header">
          <div className="section-number">DEBUG</div>
          <div>
            <h2>System & ComfyUI Diagnostics</h2>
            <p className="section-subtitle">Verify backend integrity, database health, and render pipelines</p>
          </div>
          <div className="comfy-logo">🛠️</div>
        </div>

        {/* Section A: System Integrity */}
        <div style={{ marginBottom: '32px', paddingBottom: '24px', borderBottom: '1px solid var(--border)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '16px' }}>
            <h3 style={{ fontSize: '0.9rem', textTransform: 'uppercase', color: 'var(--purple)' }}>System Integrity Tests</h3>
            <button 
              className="btn btn-secondary" 
              style={{ fontSize: '0.8rem', padding: '6px 12px' }}
              onClick={handleSystemTest}
              disabled={sysLoading}
            >
              {sysLoading ? <><Loader small /> Running...</> : '🔍 Run All Tests'}
            </button>
          </div>

          <div className="debug-grid" style={{ 
            display: 'grid', 
            gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', 
            gap: '12px' 
          }}>
            {['library', 'vectorstore', 'llm', 'character_gen'].map(key => {
              const res = sysResults?.[key] || { status: 'idle', message: 'Not tested yet' }
              return (
                <div key={key} style={{ 
                  background: 'rgba(0,0,0,0.2)', 
                  padding: '12px', 
                  borderRadius: '10px', 
                  border: `1px solid ${res.status === 'idle' ? 'var(--border)' : getStatusColor(res.status)}`
                }}>
                  <div style={{ fontSize: '0.7rem', textTransform: 'uppercase', color: 'var(--text-faint)', marginBottom: '4px' }}>{key.replace('_', ' ')}</div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '0.85rem' }}>
                    <span style={{ color: getStatusColor(res.status) }}>
                      {res.status === 'ok' ? '●' : res.status === 'warning' ? '▲' : res.status === 'error' ? '✖' : '○'}
                    </span>
                    <span style={{ fontWeight: '600' }}>{res.status.toUpperCase()}</span>
                  </div>
                  <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginTop: '4px' }}>{res.message}</div>
                </div>
              )
            })}
          </div>
        </div>

        {/* Section B: ComfyUI Diagnostics */}
        <h3 style={{ fontSize: '0.9rem', textTransform: 'uppercase', color: 'var(--purple)', marginBottom: '16px' }}>ComfyUI Render Pipeline</h3>
        
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
