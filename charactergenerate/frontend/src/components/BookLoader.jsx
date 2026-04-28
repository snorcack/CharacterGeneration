import { useState, useEffect, useRef } from 'react'
import { Loader } from './Loader'

/**
 * BookLoader — Section 01
 * Accepts book file path + name, triggers the backend indexing job,
 * and streams live progress via SSE.
 */
export default function BookLoader({ status, setStatus, progress, setProgress, onLoaded }) {
  const [file, setFile] = useState(null)
  const [bookName, setBookName] = useState('')
  const esRef = useRef(null)

  // Cleanup SSE on unmount
  useEffect(() => () => esRef.current?.close(), [])

  const handleLoad = async () => {
    if (!file || !bookName.trim()) return

    setStatus('loading')
    setProgress({ stage: '', progress: 0, total: 0, message: 'Starting…' })

    // Start the background job
    try {
      const fd = new FormData()
      fd.append('file', file)
      fd.append('book_name', bookName.trim())
      const res = await fetch('/api/upload-book', { method: 'POST', body: fd })
      if (!res.ok) {
        const data = await res.json()
        setProgress(prev => ({ ...prev, message: data.detail || 'Failed to start indexing' }))
        throw new Error('Start failed')
      }
    } catch (err) {
      setStatus('error')
      return
    }

    // Open SSE stream for live progress
    if (esRef.current) esRef.current.close()
    const es = new EventSource('/api/status')
    esRef.current = es

    es.onmessage = (e) => {
      const data = JSON.parse(e.data)
      setProgress({
        stage: data.stage || '',
        progress: data.progress ?? 0,
        total: data.total ?? 0,
        message: data.message || '',
      })

      if (data.status === 'done') {
        setStatus('done')
        onLoaded(data.characters || [])
        es.close()
      } else if (data.status === 'error') {
        setStatus('error')
        es.close()
      }
    }

    es.onerror = () => {
      setStatus('error')
      es.close()
    }
  }

  const pct =
    progress.total > 0
      ? Math.min(100, Math.round((progress.progress / progress.total) * 100))
      : 0

  const isLoading = status === 'loading'
  const isDone = status === 'done'
  const isError = status === 'error'

  return (
    <section className="glass-card">
      <div className="section-header">
        <span className="section-number">01</span>
        <div>
          <h2>Load Book</h2>
          <p className="section-subtitle">Upload a .txt or .epub file to begin indexing</p>
        </div>
      </div>

      <div className="form-row">
        <div className="form-group">
          <label htmlFor="book-file">Book File (.txt or .epub)</label>
          <input
            id="book-file"
            type="file"
            className="input"
            accept=".txt,.epub"
            onChange={(e) => {
              const f = e.target.files[0]
              if (!f) return
              setFile(f)
              setBookName(f.name.replace(/\.[^.]+$/, ''))
            }}
            disabled={isLoading}
          />
        </div>
        <div className="form-group">
          <label htmlFor="book-name">Book Name</label>
          <input
            id="book-name"
            type="text"
            className="input"
            placeholder="e.g. Eye of the World"
            value={bookName}
            onChange={(e) => setBookName(e.target.value)}
            disabled={isLoading}
            onKeyDown={(e) => e.key === 'Enter' && handleLoad()}
          />
        </div>
      </div>

      <button
        id="load-book-btn"
        className="btn btn-primary"
        onClick={handleLoad}
        disabled={!file || !bookName.trim() || isLoading}
      >
        {isLoading ? (
          <><Loader small /> Loading Book…</>
        ) : isDone ? (
          '↺ Load a Different Book'
        ) : (
          '⚡ Load Book'
        )}
      </button>

      {isLoading && (
        <div className="progress-section">
          <div className="progress-label">
            <span>{progress.message}</span>
            {progress.total > 0 && <span>{pct}%</span>}
          </div>
          <div className="progress-track">
            <div className="progress-fill" style={{ width: `${pct || 5}%` }} />
          </div>
        </div>
      )}

      {isDone && (
        <div className="success-badge">✓ Book indexed successfully — ready to generate</div>
      )}

      {isError && (
        <div className="error-badge">
          ✗ {progress.message || 'Error loading book. Check the file and try again.'}
        </div>
      )}
    </section>
  )
}
