import { useState, useEffect, useCallback, useRef } from 'react'
import { toast } from 'react-hot-toast'
import { Loader } from './Loader'
import Lightbox from './Lightbox'

// ──────────────────────────────────────────────────────────────
// Small sub-components
// ──────────────────────────────────────────────────────────────

function ImageCarousel({ images, locationName, onOpenLightbox }) {
  const [idx, setIdx] = useState(0)
  if (!images || images.length === 0) {
    return (
      <div style={{ width: '100%', aspectRatio: '16/9', background: 'rgba(0,0,0,0.3)', borderRadius: '10px', border: '1px solid var(--border)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-faint)', fontSize: '0.85rem' }}>
        🏛️ No image yet
      </div>
    )
  }
  const prev = (e) => { e.stopPropagation(); setIdx((idx - 1 + images.length) % images.length) }
  const next = (e) => { e.stopPropagation(); setIdx((idx + 1) % images.length) }

  return (
    <div className="gallery-carousel" style={{ width: '100%', aspectRatio: '16/9', borderRadius: '10px', border: '1px solid var(--border)', overflow: 'hidden', marginBottom: '12px' }}>
      <img
        src={`/api/image/${images[idx]}`}
        alt={locationName}
        style={{ width: '100%', height: '100%', objectFit: 'cover', cursor: 'zoom-in' }}
        onClick={() => onOpenLightbox(`/api/image/${images[idx]}`)}
      />
      {images.length > 1 && (
        <>
          <button className="gallery-nav-btn gallery-nav-prev" onClick={prev}>❮</button>
          <button className="gallery-nav-btn gallery-nav-next" onClick={next}>❯</button>
          <div className="gallery-dots">
            {images.map((_, i) => (
              <div key={i} className={`gallery-dot ${i === idx ? 'active' : ''}`} />
            ))}
          </div>
        </>
      )}
    </div>
  )
}

// ──────────────────────────────────────────────────────────────
// Main LocationsPanel
// ──────────────────────────────────────────────────────────────

export default function LocationsPanel({ bookName, llmProvider }) {
  // ── State ──────────────────────────────────────────────
  const [locations, setLocations] = useState([])          // list of extracted names
  const [extracting, setExtracting] = useState(false)
  const [customInput, setCustomInput] = useState('')

  const [selected, setSelected] = useState(null)          // currently active location name
  const [description, setDescription] = useState('')
  const [descLoading, setDescLoading] = useState(false)

  // Prompt generation
  const [genre, setGenre] = useState('')
  const [decade, setDecade] = useState('2026')
  const [timeOfDay, setTimeOfDay] = useState('')
  const [weather, setWeather] = useState('')
  const [prompt, setPrompt] = useState('')
  const [promptLoading, setPromptLoading] = useState(false)

  // Library data (from /api/locations)
  const [library, setLibrary] = useState({})     // { locName: { description, prompts, image_prompt_ids } }
  const [lightboxImg, setLightboxImg] = useState(null)

  // Image generation state
  const [genProvider, setGenProvider] = useState('gemini') // 'gemini' | 'comfyui'
  const [genLoading, setGenLoading] = useState(false)
  const [lastPromptId, setLastPromptId] = useState(null)
  // ComfyUI config
  const [comfyUrl, setComfyUrl] = useState('http://localhost:8188')
  const [workflowJson, setWorkflowJson] = useState('')
  const [nodeId, setNodeId] = useState('')

  // Batch agent state
  const [batchLoading, setBatchLoading] = useState(false)
  const [batchStatus, setBatchStatus] = useState({ status: 'idle', message: '', progress: 0, total: 0 })
  const [batchProvider, setBatchProvider] = useState('gemini')
  const [batchImages, setBatchImages] = useState(1)
  const [batchWorkflow, setBatchWorkflow] = useState('')
  const [batchComfyUrl, setBatchComfyUrl] = useState('http://localhost:8188')
  const [batchNodeId, setBatchNodeId] = useState('')
  const [showBatchPanel, setShowBatchPanel] = useState(false)
  const batchEsRef = useRef(null)

  // ── Load library on mount / bookName change ────────────
  const loadLibrary = useCallback(async () => {
    if (!bookName) return
    try {
      const res = await fetch(`/api/locations/${encodeURIComponent(bookName)}`)
      const data = await res.json()
      setLibrary(data.locations || {})
    } catch {
      setLibrary({})
    }
  }, [bookName])

  useEffect(() => { loadLibrary() }, [loadLibrary])

  // ── Batch agent SSE listener ─────────────────────────
  useEffect(() => {
    if (!batchLoading) return
    const es = new EventSource('/api/agent-status')
    batchEsRef.current = es
    es.onmessage = (e) => {
      const d = JSON.parse(e.data)
      setBatchStatus(d)
      if (d.status === 'done' || d.status === 'error') {
        setBatchLoading(false)
        es.close()
        if (d.status === 'done') loadLibrary()
      }
    }
    es.onerror = () => { setBatchLoading(false); es.close() }
    return () => es.close()
  }, [batchLoading])

  // ── Extract locations via RAG + LLM ───────────────────
  const handleExtract = async () => {
    setExtracting(true)
    try {
      const res = await fetch('/api/extract-locations', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ location_name: '', llm_provider: llmProvider || undefined })
      })
      if (!res.ok) throw new Error(await res.text())
      const data = await res.json()
      setLocations(data.locations || [])
      toast.success(`Found ${data.locations?.length || 0} locations!`)
    } catch (err) {
      toast.error('Extraction failed: ' + err.message)
    } finally {
      setExtracting(false)
    }
  }

  // ── Add custom location ──────────────────────────────────
  const handleBatch = async () => {
    const locsWithPrompts = Object.keys(library).filter(n => library[n]?.prompts?.length > 0)
    if (locsWithPrompts.length === 0) { toast.error('No locations with saved prompts found.'); return }
    if (batchProvider === 'comfyui' && !batchWorkflow) { toast.error('Please load a ComfyUI workflow JSON.'); return }
    setBatchLoading(true)
    setBatchStatus({ status: 'running', message: 'Starting…', progress: 0, total: locsWithPrompts.length * batchImages })
    try {
      const res = await fetch('/api/batch-generate-location-images', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          location_names: locsWithPrompts,
          images_per_location: batchImages,
          generator_type: batchProvider,
          comfy_url: batchComfyUrl,
          workflow_json: batchWorkflow,
          node_id: batchNodeId
        })
      })
      if (!res.ok) throw new Error(await res.text())
    } catch (err) {
      toast.error('Failed to start batch: ' + err.message)
      setBatchLoading(false)
    }
  }

  const handleBatchAbort = async () => {
    if (!confirm('Abort location batch generation?')) return
    await fetch('/api/abort-agent', { method: 'POST' })
    toast.success('Abort requested…')
  }

  const handleAddCustom = () => {
    const name = customInput.trim()
    if (!name || locations.includes(name)) return
    setLocations(prev => [...prev, name])
    setCustomInput('')
  }

  // ── Select a location → analyze it ────────────────────
  const handleSelectLocation = async (name) => {
    setSelected(name)
    setPrompt('')
    // If already in library, use cached description
    if (library[name]?.description) {
      setDescription(library[name].description)
      return
    }
    setDescLoading(true)
    setDescription('')
    try {
      const res = await fetch('/api/analyze-location', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ location_name: name, llm_provider: llmProvider || undefined })
      })
      if (!res.ok) throw new Error(await res.text())
      const data = await res.json()
      setDescription(data.description || '')
      await loadLibrary()
    } catch (err) {
      toast.error('Analysis failed: ' + err.message)
    } finally {
      setDescLoading(false)
    }
  }

  // ── Generate landscape prompt ─────────────────────────
  const handleGeneratePrompt = async () => {
    if (!description.trim()) return
    setPromptLoading(true)
    try {
      const res = await fetch('/api/generate-landscape-prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          book_name: bookName,
          location_name: selected,
          description,
          genre,
          decade,
          time_of_day: timeOfDay,
          weather,
          llm_provider: llmProvider || undefined
        })
      })
      if (!res.ok) throw new Error(await res.text())
      const data = await res.json()
      setPrompt(data.prompt || '')
      toast.success('Landscape prompt generated!')
    } catch (err) {
      toast.error('Prompt generation failed: ' + err.message)
    } finally {
      setPromptLoading(false)
    }
  }

  // ── Save prompt ───────────────────────────────────────
  const handleSavePrompt = async () => {
    if (!prompt || !selected || !bookName) return
    try {
      await fetch('/api/save-location-prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ book_name: bookName, location_name: selected, prompt })
      })
      await loadLibrary()
      toast.success('Prompt saved!')
    } catch (err) {
      toast.error('Save failed: ' + err.message)
    }
  }

  // ── Generate image via Gemini ─────────────────────────
  const handleGenerateGemini = async () => {
    if (!prompt) return
    setGenLoading(true)
    try {
      const res = await fetch('/api/gemini/generate-image', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt_text: prompt, aspect_ratio: '16:9' })
      })
      const reader = res.body.getReader()
      const decoder = new TextDecoder()
      let promptId = null
      while (true) {
        const { done, value } = await reader.read()
        if (done) break
        const text = decoder.decode(value)
        for (const line of text.split('\n')) {
          if (!line.startsWith('data:')) continue
          const data = JSON.parse(line.slice(5).trim())
          if (data.status === 'done') {
            promptId = data.prompt_id
          } else if (data.status === 'error') {
            throw new Error(data.message)
          }
        }
      }
      if (promptId && bookName && selected) {
        await fetch(`/api/save-location-image?book_name=${encodeURIComponent(bookName)}&location_name=${encodeURIComponent(selected)}&prompt_id=${promptId}`, { method: 'POST' })
        setLastPromptId(promptId)
        await loadLibrary()
        toast.success('Landscape image generated!')
      }
    } catch (err) {
      toast.error('Image generation failed: ' + err.message)
    } finally {
      setGenLoading(false)
    }
  }

  // ── Generate image via ComfyUI ───────────────────────
  const handleGenerateComfy = async () => {
    if (!prompt || !workflowJson) return
    setGenLoading(true)
    try {
      const res = await fetch('/api/comfyui/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ comfy_url: comfyUrl, workflow_json: workflowJson, prompt_text: prompt, node_id: nodeId || undefined })
      })
      const reader = res.body.getReader()
      const decoder = new TextDecoder()
      let promptId = null
      while (true) {
        const { done, value } = await reader.read()
        if (done) break
        for (const line of decoder.decode(value).split('\n')) {
          if (!line.startsWith('data:')) continue
          const data = JSON.parse(line.slice(5).trim())
          if (data.status === 'done') promptId = data.prompt_id
          else if (data.status === 'error') throw new Error(data.message)
        }
      }
      if (promptId && bookName && selected) {
        await fetch(`/api/save-location-image?book_name=${encodeURIComponent(bookName)}&location_name=${encodeURIComponent(selected)}&prompt_id=${promptId}`, { method: 'POST' })
        setLastPromptId(promptId)
        await loadLibrary()
        toast.success('Landscape image generated!')
      }
    } catch (err) {
      toast.error('ComfyUI generation failed: ' + err.message)
    } finally {
      setGenLoading(false)
    }
  }

  // ── Delete ────────────────────────────────────────────
  const handleDelete = async (locName, promptsOnly) => {
    if (!confirm(`Delete ${promptsOnly ? 'media' : 'all data'} for "${locName}"?`)) return
    try {
      await fetch('/api/delete-location-data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ book_name: bookName, location_name: locName, delete_prompts_only: promptsOnly })
      })
      await loadLibrary()
      if (!promptsOnly && selected === locName) setSelected(null)
      toast.success('Deleted.')
    } catch (err) {
      toast.error('Delete failed: ' + err.message)
    }
  }

  const currentEntry = library[selected] || {}
  const allLocationNames = [...new Set([...locations, ...Object.keys(library)])]

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '20px' }}>
      <Lightbox src={lightboxImg} onClose={() => setLightboxImg(null)} />

      {/* ── Header ── */}
      <div className="glass-card" style={{ padding: '24px' }}>
        <div className="section-header" style={{ marginBottom: '16px' }}>
          <span className="section-number">📍</span>
          <div>
            <h2>Location Visualizer</h2>
            <p className="section-subtitle">Extract and generate landscape images for prominent locations in the book.</p>
          </div>
        </div>

        <div style={{ display: 'flex', gap: '10px', flexWrap: 'wrap' }}>
          <button
            className="btn btn-primary"
            onClick={handleExtract}
            disabled={extracting}
            style={{ flex: 1, minWidth: '180px' }}
          >
            {extracting ? <><Loader small /> Scanning book...</> : '🗺️ Extract Locations from Book'}
          </button>
        </div>

        {/* Custom location input */}
        <div style={{ display: 'flex', gap: '8px', marginTop: '14px' }}>
          <input
            className="input"
            placeholder="Or type a location name manually..."
            value={customInput}
            onChange={e => setCustomInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && handleAddCustom()}
          />
          <button className="btn btn-secondary" onClick={handleAddCustom} disabled={!customInput.trim()}>
            Add
          </button>
        </div>

        {/* Batch agent toggle */}
        {Object.keys(library).length > 0 && (
          <div style={{ marginTop: '14px', borderTop: '1px solid var(--border)', paddingTop: '14px' }}>
            <button
              className="btn btn-secondary"
              style={{ width: '100%', justifyContent: 'space-between', borderColor: 'rgba(245,158,11,0.3)', color: 'var(--gold)' }}
              onClick={() => setShowBatchPanel(p => !p)}
            >
              <span>🚀 Batch Location Image Agent</span>
              <span>{showBatchPanel ? '▲' : '▼'}</span>
            </button>

            {showBatchPanel && (
              <div className="animate-in" style={{ marginTop: '12px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
                <div style={{ display: 'flex', gap: '8px' }}>
                  {['gemini', 'comfyui'].map(p => (
                    <button key={p} onClick={() => setBatchProvider(p)} style={{ flex: 1, padding: '7px', borderRadius: '6px', border: `1px solid ${batchProvider === p ? (p === 'gemini' ? 'var(--purple)' : 'var(--gold)') : 'var(--border)'}`, background: batchProvider === p ? (p === 'gemini' ? 'var(--purple-glow)' : 'rgba(245,158,11,0.1)') : 'transparent', color: batchProvider === p ? (p === 'gemini' ? 'var(--purple)' : 'var(--gold)') : 'var(--text-muted)', cursor: 'pointer', fontSize: '0.8rem', fontWeight: 600 }}>
                      {p === 'gemini' ? '🌐 Gemini' : '⚙️ ComfyUI'}
                    </button>
                  ))}
                </div>

                {batchProvider === 'comfyui' && (
                  <div className="animate-in" style={{ padding: '10px', background: 'rgba(245,158,11,0.04)', border: '1px solid rgba(245,158,11,0.2)', borderRadius: '8px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
                    <div className="form-group" style={{ marginBottom: 0 }}>
                      <label>ComfyUI URL</label>
                      <input className="input" value={batchComfyUrl} onChange={e => setBatchComfyUrl(e.target.value)} />
                    </div>
                    <div className="form-group" style={{ marginBottom: 0 }}>
                      <label>Workflow JSON</label>
                      <input type="file" accept=".json" style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}
                        onChange={e => { const f = e.target.files?.[0]; if (f) { const r = new FileReader(); r.onload = ev => setBatchWorkflow(ev.target.result); r.readAsText(f) } }}
                      />
                      {batchWorkflow && <span style={{ fontSize: '0.7rem', color: 'var(--success)' }}>✓ Loaded</span>}
                    </div>
                    <div className="form-group" style={{ marginBottom: 0 }}>
                      <label>Node ID (optional)</label>
                      <input className="input" placeholder="CLIPTextEncode node ID" value={batchNodeId} onChange={e => setBatchNodeId(e.target.value)} />
                    </div>
                  </div>
                )}

                <div className="form-group" style={{ marginBottom: 0 }}>
                  <label>Images per Location: <strong>{batchImages}</strong></label>
                  <input type="range" min="1" max="5" value={batchImages} onChange={e => setBatchImages(parseInt(e.target.value))} style={{ width: '100%', accentColor: 'var(--gold)' }} />
                </div>

                <button
                  className="btn btn-primary"
                  style={{ background: 'var(--gold)', color: '#000', width: '100%' }}
                  onClick={handleBatch}
                  disabled={batchLoading}
                >
                  {batchLoading ? <><Loader small /> Running…</> : '🚀 Start Batch Generation'}
                </button>

                {(batchLoading || batchStatus.status !== 'idle') && (
                  <div style={{ padding: '12px', background: 'rgba(245,158,11,0.05)', border: '1px solid rgba(245,158,11,0.2)', borderRadius: '8px' }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', marginBottom: '8px' }}>
                      <span style={{ color: 'var(--gold)', fontWeight: 600 }}>
                        {batchStatus.status === 'running' ? 'Location Agent Running…' : batchStatus.status === 'done' ? 'Done!' : batchStatus.status === 'error' ? 'Error' : ''}
                      </span>
                      <span style={{ color: 'var(--text-faint)' }}>{batchStatus.progress} / {batchStatus.total}</span>
                    </div>
                    {batchStatus.status === 'running' && (
                      <button className="btn btn-secondary" style={{ width: '100%', marginBottom: '8px', fontSize: '0.75rem', borderColor: 'rgba(255,107,107,0.3)', color: '#ff6b6b' }} onClick={handleBatchAbort}>
                        🛑 Abort
                      </button>
                    )}
                    <div style={{ height: '5px', background: 'rgba(0,0,0,0.2)', borderRadius: '3px', overflow: 'hidden' }}>
                      <div style={{ height: '100%', background: 'var(--gold)', width: `${batchStatus.total > 0 ? (batchStatus.progress / batchStatus.total) * 100 : 0}%`, transition: 'width 0.4s ease' }} />
                    </div>
                    <div style={{ marginTop: '6px', fontSize: '0.73rem', color: 'var(--text-muted)', fontStyle: 'italic' }}>{batchStatus.message}</div>
                  </div>
                )}
              </div>
            )}
          </div>
        )}
      </div>

      {/* ── Two-column layout ── */}
      {allLocationNames.length > 0 && (
        <div style={{ display: 'grid', gridTemplateColumns: '260px 1fr', gap: '20px', alignItems: 'start' }}>

          {/* ── Left: Location list ── */}
          <div className="glass-card" style={{ padding: '16px' }}>
            <h3 style={{ fontSize: '0.8rem', color: 'var(--text-faint)', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.08em', marginBottom: '12px' }}>
              Locations ({allLocationNames.length})
            </h3>
            <div style={{ display: 'flex', flexDirection: 'column', gap: '6px', maxHeight: '60vh', overflowY: 'auto' }}>
              {allLocationNames.map(name => {
                const inLibrary = !!library[name]
                const hasImage = (library[name]?.image_prompt_ids || []).length > 0
                return (
                  <button
                    key={name}
                    onClick={() => handleSelectLocation(name)}
                    style={{
                      display: 'flex', alignItems: 'center', gap: '8px',
                      padding: '10px 12px', borderRadius: '8px',
                      background: selected === name ? 'var(--purple-glow)' : 'rgba(0,0,0,0.15)',
                      border: `1px solid ${selected === name ? 'var(--purple)' : 'var(--border)'}`,
                      cursor: 'pointer', textAlign: 'left', width: '100%',
                      color: selected === name ? 'var(--purple)' : 'var(--text-muted)',
                      fontSize: '0.85rem', fontWeight: 600,
                      transition: 'all 0.2s'
                    }}
                  >
                    <span style={{ fontSize: '1rem' }}>{hasImage ? '🖼️' : inLibrary ? '📝' : '📍'}</span>
                    <span style={{ flex: 1, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{name}</span>
                  </button>
                )
              })}
            </div>
          </div>

          {/* ── Right: Detail panel ── */}
          <div style={{ display: 'flex', flexDirection: 'column', gap: '16px' }}>
            {selected ? (
              <>
                {/* Description */}
                <div className="glass-card" style={{ padding: '20px' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '12px' }}>
                    <h3 style={{ color: 'var(--purple)', fontSize: '1.1rem', fontWeight: 700 }}>{selected}</h3>
                    <div style={{ display: 'flex', gap: '8px' }}>
                      <button className="btn btn-secondary" style={{ fontSize: '0.7rem', padding: '4px 10px', color: '#ff6b6b', borderColor: 'rgba(255,107,107,0.3)' }} onClick={() => handleDelete(selected, false)}>
                        🗑️ Delete
                      </button>
                      <button className="btn btn-secondary" style={{ fontSize: '0.7rem', padding: '4px 10px' }} onClick={() => handleDelete(selected, true)} disabled={!currentEntry.prompts?.length && !currentEntry.image_prompt_ids?.length}>
                        Clear Media
                      </button>
                    </div>
                  </div>

                  {descLoading ? (
                    <div className="loading-row">
                      <Loader /> <span>Analyzing location from book passages…</span>
                    </div>
                  ) : (
                    <textarea
                      className="textarea"
                      rows={6}
                      value={description}
                      onChange={e => setDescription(e.target.value)}
                      placeholder="Location description will appear here…"
                    />
                  )}
                </div>

                {/* Image carousel */}
                {(currentEntry.image_prompt_ids || []).length > 0 && (
                  <div className="glass-card" style={{ padding: '16px' }}>
                    <h4 style={{ fontSize: '0.8rem', color: 'var(--text-faint)', marginBottom: '10px', textTransform: 'uppercase', letterSpacing: '0.07em' }}>
                      Generated Images ({currentEntry.image_prompt_ids.length})
                    </h4>
                    <ImageCarousel images={currentEntry.image_prompt_ids} locationName={selected} onOpenLightbox={setLightboxImg} />
                  </div>
                )}

                {/* Prompt generation controls */}
                {description && !descLoading && (
                  <div className="glass-card" style={{ padding: '20px' }}>
                    <h4 style={{ fontSize: '0.85rem', color: 'var(--text-muted)', marginBottom: '14px', textTransform: 'uppercase', letterSpacing: '0.07em' }}>
                      🎨 Generate Landscape Image Prompt
                    </h4>

                    <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '10px', marginBottom: '14px' }}>
                      <div className="form-group" style={{ marginBottom: 0 }}>
                        <label>Genre / Style</label>
                        <input className="input" placeholder="e.g. Gothic, Steampunk, Pastoral" value={genre} onChange={e => setGenre(e.target.value)} />
                      </div>
                      <div className="form-group" style={{ marginBottom: 0 }}>
                        <label>Decade</label>
                        <div className="select-wrapper">
                          <select className="select" value={decade} onChange={e => setDecade(e.target.value)}>
                            <option value="2026">Modern (2026)</option>
                            <option value="2010">2010s</option>
                            <option value="2000">2000s</option>
                            <option value="1990">1990s</option>
                            <option value="1980">1980s</option>
                            <option value="1970">1970s</option>
                            <option value="1950">1950s</option>
                            <option value="1900">1900s / Period</option>
                          </select>
                        </div>
                      </div>
                      <div className="form-group" style={{ marginBottom: 0 }}>
                        <label>Time of Day</label>
                        <div className="select-wrapper">
                          <select className="select" value={timeOfDay} onChange={e => setTimeOfDay(e.target.value)}>
                            <option value="">Any</option>
                            <option value="golden hour sunrise">Golden Hour (Sunrise)</option>
                            <option value="morning">Morning</option>
                            <option value="midday">Midday</option>
                            <option value="golden hour sunset">Golden Hour (Sunset)</option>
                            <option value="blue hour">Blue Hour</option>
                            <option value="night">Night</option>
                            <option value="stormy">Stormy / Dramatic</option>
                          </select>
                        </div>
                      </div>
                      <div className="form-group" style={{ marginBottom: 0 }}>
                        <label>Weather</label>
                        <div className="select-wrapper">
                          <select className="select" value={weather} onChange={e => setWeather(e.target.value)}>
                            <option value="">Clear / Default</option>
                            <option value="heavy rain and puddles">Heavy Rain</option>
                            <option value="light fog and mist">Fog & Mist</option>
                            <option value="overcast and moody">Overcast</option>
                            <option value="dramatic storm with lightning">Stormy</option>
                            <option value="light snow falling">Snow</option>
                            <option value="heat haze and dry dust">Heat Haze</option>
                          </select>
                        </div>
                      </div>
                    </div>

                    <button
                      className="btn btn-primary generate-btn"
                      onClick={handleGeneratePrompt}
                      disabled={promptLoading || !description.trim()}
                    >
                      {promptLoading ? <><Loader small /> Generating prompt…</> : '✨ Generate Landscape Prompt'}
                    </button>

                    {prompt && (
                      <div style={{ marginTop: '16px' }}>
                        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
                          <label style={{ fontSize: '0.75rem', color: 'var(--text-faint)', textTransform: 'uppercase', letterSpacing: '0.07em' }}>Generated Prompt</label>
                          <div style={{ display: 'flex', gap: '8px' }}>
                            <button className="btn btn-secondary" style={{ fontSize: '0.7rem', padding: '4px 10px' }} onClick={handleSavePrompt}>
                              💾 Save
                            </button>
                            <button className="btn btn-secondary" style={{ fontSize: '0.7rem', padding: '4px 10px' }} onClick={() => { navigator.clipboard.writeText(prompt); toast.success('Copied!') }}>
                              📋 Copy
                            </button>
                          </div>
                        </div>
                        <textarea
                          className="textarea"
                          rows={6}
                          value={prompt}
                          onChange={e => setPrompt(e.target.value)}
                          style={{ fontSize: '0.8rem', lineHeight: '1.6' }}
                        />

                        {/* Provider selector */}
                        <div style={{ display: 'flex', gap: '8px', marginTop: '12px', padding: '10px', background: 'rgba(0,0,0,0.2)', borderRadius: '8px', border: '1px solid var(--border)' }}>
                          <button
                            onClick={() => setGenProvider('gemini')}
                            style={{ flex: 1, padding: '8px', borderRadius: '6px', border: `1px solid ${genProvider === 'gemini' ? 'var(--purple)' : 'var(--border)'}`, background: genProvider === 'gemini' ? 'var(--purple-glow)' : 'transparent', color: genProvider === 'gemini' ? 'var(--purple)' : 'var(--text-muted)', cursor: 'pointer', fontSize: '0.8rem', fontWeight: 600 }}
                          >🌐 Gemini</button>
                          <button
                            onClick={() => setGenProvider('comfyui')}
                            style={{ flex: 1, padding: '8px', borderRadius: '6px', border: `1px solid ${genProvider === 'comfyui' ? 'var(--gold)' : 'var(--border)'}`, background: genProvider === 'comfyui' ? 'rgba(245,158,11,0.1)' : 'transparent', color: genProvider === 'comfyui' ? 'var(--gold)' : 'var(--text-muted)', cursor: 'pointer', fontSize: '0.8rem', fontWeight: 600 }}
                          >⚙️ ComfyUI</button>
                        </div>

                        {genProvider === 'comfyui' && (
                          <div className="animate-in" style={{ marginTop: '10px', display: 'flex', flexDirection: 'column', gap: '8px', padding: '10px', background: 'rgba(245,158,11,0.04)', border: '1px solid rgba(245,158,11,0.2)', borderRadius: '8px' }}>
                            <div className="form-group" style={{ marginBottom: 0 }}>
                              <label>ComfyUI URL</label>
                              <input className="input" value={comfyUrl} onChange={e => setComfyUrl(e.target.value)} />
                            </div>
                            <div className="form-group" style={{ marginBottom: 0 }}>
                              <label>Workflow JSON</label>
                              <input type="file" accept=".json" style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}
                                onChange={e => { const f = e.target.files?.[0]; if (f) { const r = new FileReader(); r.onload = ev => setWorkflowJson(ev.target.result); r.readAsText(f) } }}
                              />
                              {workflowJson && <span style={{ fontSize: '0.7rem', color: 'var(--success)' }}>✓ JSON Loaded</span>}
                            </div>
                            <div className="form-group" style={{ marginBottom: 0 }}>
                              <label>Node ID (optional)</label>
                              <input className="input" placeholder="CLIPTextEncode node ID" value={nodeId} onChange={e => setNodeId(e.target.value)} />
                            </div>
                          </div>
                        )}

                        <button
                          className="btn comfy-gen-btn"
                          style={{ width: '100%', marginTop: '10px', justifyContent: 'center', color: '#fff' }}
                          onClick={genProvider === 'gemini' ? handleGenerateGemini : handleGenerateComfy}
                          disabled={genLoading || (genProvider === 'comfyui' && !workflowJson)}
                        >
                          {genLoading
                            ? <><Loader small /> Generating image…</>
                            : genProvider === 'gemini' ? '🖼️ Generate via Gemini' : '⚙️ Generate via ComfyUI'}
                        </button>
                      </div>
                    )}
                  </div>
                )}

                {/* Saved prompts */}
                {(currentEntry.prompts || []).length > 0 && (
                  <div className="glass-card" style={{ padding: '16px' }}>
                    <h4 style={{ fontSize: '0.8rem', color: 'var(--text-faint)', marginBottom: '10px', textTransform: 'uppercase', letterSpacing: '0.07em' }}>
                      Saved Prompts ({currentEntry.prompts.length})
                    </h4>
                    <div style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                      {currentEntry.prompts.map((p, i) => (
                        <div key={i} style={{ padding: '10px', background: 'rgba(0,0,0,0.2)', border: '1px solid var(--border)', borderRadius: '8px', fontSize: '0.78rem', lineHeight: '1.5' }}>
                          <div style={{ display: 'flex', justifyContent: 'flex-end', gap: '6px', marginBottom: '6px' }}>
                            <button className="btn btn-secondary" style={{ fontSize: '0.65rem', padding: '3px 8px' }} onClick={() => setPrompt(p)}>
                              ↩ Use
                            </button>
                            <button className="btn btn-secondary" style={{ fontSize: '0.65rem', padding: '3px 8px' }} onClick={() => { navigator.clipboard.writeText(p); toast.success('Copied!') }}>
                              📋
                            </button>
                          </div>
                          {p}
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </>
            ) : (
              <div className="glass-card" style={{ padding: '60px 40px', textAlign: 'center', color: 'var(--text-faint)' }}>
                <div style={{ fontSize: '3rem', marginBottom: '16px' }}>🏛️</div>
                <h3 style={{ color: 'var(--text-muted)', marginBottom: '8px' }}>Select a Location</h3>
                <p style={{ fontSize: '0.85rem' }}>Choose a location from the list to analyze and generate landscape images.</p>
              </div>
            )}
          </div>
        </div>
      )}

      {/* Empty state */}
      {allLocationNames.length === 0 && !extracting && (
        <div className="glass-card" style={{ padding: '60px 40px', textAlign: 'center', color: 'var(--text-faint)' }}>
          <div style={{ fontSize: '3.5rem', marginBottom: '16px', animation: 'pulseObj 2s infinite' }}>🗺️</div>
          <h3 style={{ color: 'var(--text)', marginBottom: '8px' }}>No Locations Yet</h3>
          <p style={{ marginBottom: '20px', fontSize: '0.9rem' }}>Click <strong>"Extract Locations from Book"</strong> to automatically find prominent places, or type a location name above.</p>
        </div>
      )}
    </div>
  )
}
