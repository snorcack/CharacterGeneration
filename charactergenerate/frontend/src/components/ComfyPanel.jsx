import { useState, useRef, useCallback } from 'react'
import { Loader } from './Loader'

const STATUS_ICONS = {
  idle: '🎨',
  injecting: '⚙️',
  queued: '⏳',
  polling: '🔄',
  fetching: '⬇️',
  done: '✅',
  error: '❌',
}

const STATUS_COLORS = {
  idle: 'var(--text-muted)',
  injecting: 'var(--purple)',
  queued: 'var(--gold)',
  polling: 'var(--purple)',
  fetching: 'var(--purple)',
  done: 'var(--success)',
  error: 'var(--error)',
}

/**
 * ComfyPanel — Section 05
 * Connect to a local ComfyUI instance, upload an API-format workflow JSON,
 * inject the generated prompt, and display the resulting image.
 */
export default function ComfyPanel({ prompt }) {
  const [comfyUrl, setComfyUrl] = useState('http://localhost:8188')
  const [nodeId, setNodeId] = useState('')
  const [workflowFile, setWorkflowFile] = useState(null)       // File object
  const [workflowJson, setWorkflowJson] = useState('')          // raw JSON string
  const [testStatus, setTestStatus] = useState(null)            // null | 'ok' | 'error'
  const [testMsg, setTestMsg] = useState('')
  const [testLoading, setTestLoading] = useState(false)

  const [genStatus, setGenStatus] = useState('idle')            // idle | injecting | queued | polling | fetching | done | error
  const [genMessage, setGenMessage] = useState('')
  const [promptId, setPromptId] = useState(null)
  const [imageUrl, setImageUrl] = useState(null)
  const [showAdvanced, setShowAdvanced] = useState(false)

  const fileInputRef = useRef(null)
  const abortRef = useRef(null)

  /* ── Test connection ──────────────────────────────────────────── */
  const handleTest = useCallback(async () => {
    setTestLoading(true)
    setTestStatus(null)
    setTestMsg('')
    try {
      const res = await fetch('/api/comfyui/test', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ comfy_url: comfyUrl }),
      })
      if (res.ok) {
        setTestStatus('ok')
        setTestMsg('ComfyUI is reachable ✓')
      } else {
        const err = await res.json()
        setTestStatus('error')
        setTestMsg(err.detail || 'Connection failed')
      }
    } catch {
      setTestStatus('error')
      setTestMsg('Network error — is ComfyUI running?')
    } finally {
      setTestLoading(false)
    }
  }, [comfyUrl])

  /* ── File upload ──────────────────────────────────────────────── */
  const handleFileChange = useCallback((e) => {
    const file = e.target.files?.[0]
    if (!file) return
    setWorkflowFile(file)
    const reader = new FileReader()
    reader.onload = (ev) => setWorkflowJson(ev.target.result)
    reader.readAsText(file)
  }, [])

  const handleDrop = useCallback((e) => {
    e.preventDefault()
    const file = e.dataTransfer.files?.[0]
    if (!file || !file.name.endsWith('.json')) return
    setWorkflowFile(file)
    const reader = new FileReader()
    reader.onload = (ev) => setWorkflowJson(ev.target.result)
    reader.readAsText(file)
  }, [])

  /* ── Generate image ───────────────────────────────────────────── */
  const handleGenerate = useCallback(async () => {
    if (!workflowJson || !prompt) return

    setGenStatus('injecting')
    setGenMessage('Preparing…')
    setPromptId(null)
    setImageUrl(null)

    const body = JSON.stringify({
      comfy_url: comfyUrl,
      workflow_json: workflowJson,
      prompt_text: prompt,
      node_id: nodeId.trim() || null,
    })

    const es = new EventSource('/api/comfyui/generate?' + new URLSearchParams({ _body: body }))
    // EventSource doesn't support POST; use fetch with streaming instead
    es.close()

    let reader
    try {
      const response = await fetch('/api/comfyui/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body,
      })
      if (!response.ok) {
        const err = await response.json()
        setGenStatus('error')
        setGenMessage(err.detail || 'Request failed')
        return
      }

      reader = response.body.getReader()
      abortRef.current = () => reader.cancel()
      const decoder = new TextDecoder()
      let buffer = ''

      while (true) {
        const { done, value } = await reader.read()
        if (done) break
        buffer += decoder.decode(value, { stream: true })
        const lines = buffer.split('\n')
        buffer = lines.pop()          // keep incomplete line

        for (const line of lines) {
          if (!line.startsWith('data: ')) continue
          try {
            const evt = JSON.parse(line.slice(6))
            setGenStatus(evt.status)
            setGenMessage(evt.message || '')
            if (evt.prompt_id) setPromptId(evt.prompt_id)
            if (evt.status === 'done' && evt.prompt_id) {
              setImageUrl(`/api/comfyui/image/${evt.prompt_id}?ts=${Date.now()}`)
            }
          } catch { /* malformed line */ }
        }
      }
    } catch (err) {
      setGenStatus('error')
      setGenMessage(err.message || 'Streaming error')
    }
  }, [comfyUrl, workflowJson, prompt, nodeId])

  const canGenerate = !!workflowJson && !!prompt && genStatus !== 'injecting' &&
    genStatus !== 'queued' && genStatus !== 'polling' && genStatus !== 'fetching'

  const isGenerating = ['injecting', 'queued', 'polling', 'fetching'].includes(genStatus)

  /* ── Render ───────────────────────────────────────────────────── */
  return (
    <section className="glass-card comfy-panel animate-in">
      {/* Header */}
      <div className="section-header">
        <span className="section-number">05</span>
        <div>
          <h2 style={{fontSize: '1.2rem'}}>ComfyUI Gen</h2>
          <p className="section-subtitle">
            Local render pipeline
          </p>
        </div>
      </div>

      {/* URL + Test row */}
      <div className="comfy-url-row">
        <div className="form-group flex-1" style={{ marginBottom: 0 }}>
          <label htmlFor="comfy-url-input">ComfyUI Server URL</label>
          <input
            id="comfy-url-input"
            className="input"
            type="text"
            value={comfyUrl}
            onChange={e => { setComfyUrl(e.target.value); setTestStatus(null) }}
            placeholder="http://localhost:8188"
          />
        </div>
        <button
          id="comfy-test-btn"
          className={`btn btn-secondary comfy-test-btn ${testStatus === 'ok' ? 'test-ok' : testStatus === 'error' ? 'test-err' : ''}`}
          onClick={handleTest}
          disabled={testLoading}
        >
          {testLoading ? <><Loader small /> Testing…</> : '🔌 Test'}
        </button>
      </div>

      {testStatus && (
        <div className={testStatus === 'ok' ? 'comfy-status-ok' : 'comfy-status-err'}>
          {testMsg}
        </div>
      )}

      {/* Workflow file drop */}
      <div
        className={`file-drop-zone ${workflowFile ? 'file-loaded' : ''}`}
        onDrop={handleDrop}
        onDragOver={e => e.preventDefault()}
        onClick={() => fileInputRef.current?.click()}
      >
        <input
          ref={fileInputRef}
          type="file"
          accept=".json"
          style={{ display: 'none' }}
          onChange={handleFileChange}
          id="workflow-file-input"
        />
        {workflowFile ? (
          <div className="file-drop-loaded">
            <span className="file-icon">📄</span>
            <div>
              <div className="file-name">{workflowFile.name}</div>
              <div className="file-hint">Click to replace</div>
            </div>
            <span className="file-check">✓</span>
          </div>
        ) : (
          <div className="file-drop-prompt">
            <span className="file-drop-icon">📂</span>
            <div>
              <div className="file-drop-title">Drop workflow JSON here</div>
              <div className="file-drop-sub">or click to browse — API-format export from ComfyUI</div>
            </div>
          </div>
        )}
      </div>

      {/* Advanced: node override */}
      <button
        className="comfy-advanced-toggle"
        onClick={() => setShowAdvanced(v => !v)}
      >
        {showAdvanced ? '▾' : '▸'} Advanced options
      </button>

      {showAdvanced && (
        <div className="comfy-advanced animate-in">
          <div className="form-group">
            <label htmlFor="node-id-input">
              Node ID override
              <span className="label-hint">— leave blank to auto-detect CLIPTextEncode</span>
            </label>
            <input
              id="node-id-input"
              className="input"
              type="text"
              value={nodeId}
              onChange={e => setNodeId(e.target.value)}
              placeholder="e.g. 6"
            />
          </div>
        </div>
      )}

      {/* Generate button */}
      <button
        id="comfy-generate-btn"
        className="btn btn-primary generate-btn comfy-gen-btn"
        onClick={handleGenerate}
        disabled={!canGenerate}
      >
        {isGenerating ? (
          <><Loader small /> {STATUS_ICONS[genStatus]} Generating…</>
        ) : genStatus === 'done' ? (
          '🔄 Regenerate Image'
        ) : (
          '🎨 Generate Image with ComfyUI'
        )}
      </button>

      {/* Progress */}
      {(isGenerating || genStatus === 'done' || genStatus === 'error') && (
        <div className="comfy-progress-bar">
          <div className="comfy-progress-label">
            <span style={{ color: STATUS_COLORS[genStatus] }}>
              {STATUS_ICONS[genStatus]} {genMessage}
            </span>
            {promptId && (
              <span className="comfy-prompt-id">{promptId.slice(0, 8)}…</span>
            )}
          </div>
          {isGenerating && (
            <div className="progress-track" style={{ marginTop: 8 }}>
              <div className="progress-fill comfy-indeterminate" />
            </div>
          )}
        </div>
      )}

      {/* Image output */}
      {imageUrl && genStatus === 'done' && (
        <div className="comfy-image-frame animate-in">
          <div className="comfy-image-header">
            <span>🖼 Generated Portrait</span>
            <a
              href={imageUrl}
              download="character_portrait.png"
              className="btn-copy"
              id="comfy-download-btn"
            >
              ⬇ Download
            </a>
          </div>
          <img
            src={imageUrl}
            alt="AI generated character portrait"
            className="comfy-image"
            onLoad={e => e.target.classList.add('comfy-image-reveal')}
          />
        </div>
      )}
    </section>
  )
}
