import { useState, useEffect, useRef } from 'react'
import { Loader } from './Loader'
import { useTasks } from '../context/TaskContext'

export default function BatchImageGenerator({ bookName, onAgentDone, initiallyOpen = false }) {
  const [charactersWithPrompts, setCharactersWithPrompts] = useState([])
  const [selectedChars, setSelectedChars] = useState([])
  const [imagesPerChar, setImagesPerChar] = useState(1)
  const [imageProvider, setImageProvider] = useState('comfyui')
  const [comfyUrl, setComfyUrl] = useState('http://localhost:8188')
  const [workflowJson, setWorkflowJson] = useState('')
  const [nodeId, setNodeId] = useState('')
  const [geminiModel, setGeminiModel] = useState('gemini-3.1-flash-image-preview')
  
  const [loadingChars, setLoadingChars] = useState(false)
  const [agentLoading, setAgentLoading] = useState(false)
  const [agentStatus, setAgentStatus] = useState({ status: 'idle', message: '', progress: 0, total: 0 })
  const [isOpen, setIsOpen] = useState(initiallyOpen)
  const { setTaskProgress, clearTask } = useTasks()

  const fileInputRef = useRef(null)

  useEffect(() => {
    if (isOpen && bookName) {
      loadCharacters()
    }
  }, [isOpen, bookName])

  const loadCharacters = async () => {
    setLoadingChars(true)
    try {
      const res = await fetch(`/api/character-descriptions/${encodeURIComponent(bookName)}`)
      const data = await res.json()
      const chars = Object.entries(data.descriptions || {})
        .filter(([_, entry]) => entry.prompts && entry.prompts.length > 0)
        .map(([name, _]) => name)
      setCharactersWithPrompts(chars)
    } catch (err) {
      console.error('Failed to load characters:', err)
    } finally {
      setLoadingChars(false)
    }
  }

  useEffect(() => {
    let eventSource = null
    if (agentLoading) {
      eventSource = new EventSource('/api/agent-status')
      eventSource.onmessage = (event) => {
        const data = JSON.parse(event.data)
        setAgentStatus(data)
        
        setTaskProgress('batch-image-agent', { 
          title: 'Batch Image Generator', 
          status: data.status === 'done' ? 'done' : 'running', 
          progress: data.progress, 
          total: data.total, 
          message: data.message 
        })
        
        if (data.status === 'done' || data.status === 'error') {
          setAgentLoading(false)
          eventSource.close()
          if (data.status === 'error') {
            setTaskProgress('batch-image-agent', { title: 'Batch Image Generator', status: 'error', message: data.message || 'Agent error' })
          } else {
            setTimeout(() => clearTask('batch-image-agent'), 3000)
          }
          if (data.status === 'done' && onAgentDone) {
            onAgentDone()
          }
        }
      }
      eventSource.onerror = () => {
        setAgentLoading(false)
        setTaskProgress('batch-image-agent', { title: 'Batch Image Generator', status: 'error', message: 'SSE Connection lost' })
        eventSource.close()
      }
    }
    return () => {
      if (eventSource) eventSource.close()
    }
  }, [agentLoading, onAgentDone])

  const toggleChar = (char) => {
    setSelectedChars(prev => 
      prev.includes(char) 
        ? prev.filter(c => c !== char) 
        : [...prev, char]
    )
  }

  const handleFileChange = (e) => {
    const file = e.target.files?.[0]
    if (!file) return
    const reader = new FileReader()
    reader.onload = (ev) => setWorkflowJson(ev.target.result)
    reader.readAsText(file)
  }

  const handleStartGeneration = async () => {
    if (selectedChars.length === 0) {
      alert('Please select at least one character.')
      return
    }
    if (imageProvider === 'comfyui' && !workflowJson) {
      alert('Please provide a ComfyUI workflow JSON.')
      return
    }

    setAgentLoading(true)
    setAgentStatus({ 
      status: 'running', 
      message: 'Starting batch image generation...', 
      progress: 0, 
      total: selectedChars.length * imagesPerChar 
    })

    try {
      const res = await fetch('/api/batch-generate-images', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          character_names: selectedChars,
          images_per_character: imagesPerChar,
          generator_type: imageProvider,
          comfy_url: comfyUrl,
          workflow_json: workflowJson,
          node_id: nodeId,
          gemini_model: geminiModel
        })
      })
      if (!res.ok) throw new Error(await res.text())
    } catch (err) {
      console.error(err)
      setAgentStatus({ status: 'error', message: 'Failed to start agent: ' + err.message, progress: 0, total: 0 })
      setAgentLoading(false)
    }
  }
  
  const handleAbort = async () => {
    if (!confirm('Are you sure you want to abort the image generation?')) return
    try {
      const res = await fetch('/api/abort-agent', { method: 'POST' })
      if (!res.ok) throw new Error('Failed to abort')
      toast.success('Abort requested...')
    } catch (err) {
      console.error(err)
      toast.error('Failed to abort: ' + err.message)
    }
  }

  return (
    <div className="batch-image-generator glass-card animate-in" style={{ marginTop: '20px' }}>
      <button 
        className="btn btn-secondary" 
        style={{ width: '100%', justifyContent: 'space-between', border: '1px solid var(--gold)' }}
        onClick={() => setIsOpen(!isOpen)}
      >
        <span>🖼 Batch Image Agent</span>
        <span>{isOpen ? '▲' : '▼'}</span>
      </button>

      {isOpen && (
        <div style={{ marginTop: '16px' }}>
          <p className="section-subtitle" style={{ marginBottom: '12px' }}>
            Generate images in bulk for characters with saved prompts.
          </p>

          <div className="form-group">
            <label>Image Provider</label>
            <select 
              className="select" 
              value={imageProvider}
              onChange={e => setImageProvider(e.target.value)}
            >
              <option value="comfyui">ComfyUI (Local)</option>
              <option value="gemini">Gemini (Cloud)</option>
            </select>
          </div>

          {imageProvider === 'comfyui' && (
            <div className="animate-in" style={{ marginBottom: '16px', padding: '12px', background: 'rgba(255,255,255,0.02)', borderRadius: '8px', border: '1px solid var(--border)' }}>
              <div className="form-group">
                <label>ComfyUI Server URL</label>
                <input type="text" className="input" value={comfyUrl} onChange={e => setComfyUrl(e.target.value)} />
              </div>
              <div className="form-group">
                <label>Workflow JSON</label>
                <input type="file" accept=".json" onChange={handleFileChange} style={{ fontSize: '0.8rem' }} />
                {workflowJson && <span style={{ fontSize: '0.7rem', color: 'var(--success)' }}>✓ JSON Loaded</span>}
              </div>
              <div className="form-group" style={{ marginBottom: 0 }}>
                <label>Node ID (Optional)</label>
                <input type="text" className="input" placeholder="CLIPTextEncode node ID" value={nodeId} onChange={e => setNodeId(e.target.value)} />
              </div>
            </div>
          )}

          {imageProvider === 'gemini' && (
            <div className="animate-in" style={{ marginBottom: '16px' }}>
              <div className="form-group">
                <label>Gemini Image Model</label>
                <input type="text" className="input" value={geminiModel} onChange={e => setGeminiModel(e.target.value)} />
              </div>
            </div>
          )}

          <div className="form-group">
            <label>Images Per Character: <strong>{imagesPerChar}</strong></label>
            <input 
              type="range" 
              min="1" 
              max="5" 
              value={imagesPerChar} 
              onChange={e => setImagesPerChar(parseInt(e.target.value))} 
              style={{ width: '100%', accentColor: 'var(--gold)' }}
            />
          </div>

          <label style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: '8px', display: 'block' }}>
            SELECT CHARACTERS ({charactersWithPrompts.length} available)
          </label>
          
          <div className="char-checklist" style={{ 
            maxHeight: '150px', 
            overflowY: 'auto', 
            background: 'rgba(0,0,0,0.1)', 
            padding: '10px',
            borderRadius: '8px',
            marginBottom: '16px',
            display: 'grid',
            gridTemplateColumns: '1fr 1fr',
            gap: '8px'
          }}>
            {loadingChars ? <Loader small /> : (
              charactersWithPrompts.length > 0 ? (
                charactersWithPrompts.map(char => (
                  <label key={char} style={{ 
                    display: 'flex', 
                    alignItems: 'center', 
                    gap: '8px', 
                    fontSize: '0.85rem', 
                    cursor: 'pointer',
                    color: selectedChars.includes(char) ? 'var(--gold)' : 'var(--text-muted)'
                  }}>
                    <input 
                      type="checkbox" 
                      checked={selectedChars.includes(char)}
                      onChange={() => toggleChar(char)}
                      style={{ accentColor: 'var(--gold)' }}
                    />
                    {char}
                  </label>
                ))
              ) : (
                <div style={{ gridColumn: 'span 2', textAlign: 'center', fontSize: '0.8rem', color: 'var(--text-faint)', padding: '10px' }}>
                  No characters with prompts found. Generate prompts first!
                </div>
              )
            )}
          </div>

          <button 
            className="btn btn-primary" 
            style={{ width: '100%', background: 'var(--gold)', color: '#000' }}
            onClick={handleStartGeneration}
            disabled={agentLoading || selectedChars.length === 0}
          >
            {agentLoading ? <Loader small /> : '🚀 Start Batch Generation'}
          </button>

          {(agentLoading || agentStatus.status !== 'idle') && (
            <div className="agent-progress-box" style={{ 
              padding: '12px', 
              background: 'rgba(245, 158, 11, 0.05)', 
              border: '1px solid rgba(245, 158, 11, 0.2)',
              borderRadius: '8px',
              marginTop: '16px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', marginBottom: '8px' }}>
                <span style={{ color: 'var(--gold)', fontWeight: '600' }}>
                  {agentStatus.status === 'running' ? 'Image Agent Running...' : 
                   agentStatus.status === 'done' ? 'Bulk Generation Done!' : 
                   agentStatus.status === 'error' ? 'Agent Error' : ''}
                </span>
                <span style={{ color: 'var(--text-faint)' }}>
                  {agentStatus.progress} / {agentStatus.total}
                </span>
              </div>
              
              {agentStatus.status === 'running' && (
                <button 
                  className="btn btn-secondary" 
                  style={{ width: '100%', marginBottom: '10px', fontSize: '0.75rem', borderColor: 'rgba(255,107,107,0.3)', color: '#ff6b6b' }}
                  onClick={handleAbort}
                >
                  🛑 Abort Generation
                </button>
              )}

              <div className="progress-bar-bg" style={{ height: '6px', background: 'rgba(0,0,0,0.2)', borderRadius: '3px', overflow: 'hidden' }}>
                <div 
                  className="progress-bar-fill" 
                  style={{ 
                    height: '100%', 
                    background: 'var(--gold)', 
                    width: `${agentStatus.total > 0 ? (agentStatus.progress / agentStatus.total) * 100 : 0}%`,
                    transition: 'width 0.4s ease'
                  }}
                />
              </div>
              <div style={{ marginTop: '8px', fontSize: '0.75rem', color: 'var(--text-muted)', fontStyle: 'italic' }}>
                {agentStatus.message}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
