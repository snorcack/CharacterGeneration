import { useState, useEffect, useRef } from 'react'
import { Loader } from './Loader'
import { useTasks } from '../context/TaskContext'

/**
 * BookLoader — Section 01
 * Accepts book file path + name, triggers the backend indexing job,
 * and streams live progress via SSE.
 */
export default function BookLoader({ status, setStatus, progress, setProgress, onLoaded }) {
  const [bookPath, setBookPath] = useState('')
  const [bookName, setBookName] = useState('')
  const [library, setLibrary] = useState({})
  const [useExisting, setUseExisting] = useState(false)
  const esRef = useRef(null)
  const { setTaskProgress, clearTask } = useTasks()

  // Fetch existing library on mount
  useEffect(() => {
    fetch('/api/books')
      .then(res => res.json())
      .then(data => {
        setLibrary(data)
        if (Object.keys(data).length > 0) {
          setUseExisting(true)
          const firstBook = Object.keys(data)[0]
          setBookName(firstBook)
          setBookPath(data[firstBook].book_path)
        }
      })
      .catch(() => {})
  }, [])

  // Cleanup SSE on unmount
  useEffect(() => () => esRef.current?.close(), [])

  const handleLoad = async () => {
    if (!bookPath.trim() || !bookName.trim()) return

    setStatus('loading')
    setProgress({ stage: '', progress: 0, total: 0, message: 'Starting…' })

    // Start the background job
    try {
      const res = await fetch('/api/load-book', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ book_path: bookPath.trim(), book_name: bookName.trim() }),
      })
      if (!res.ok) {
        const data = await res.json()
        const errMsg = data.detail || 'Failed to start indexing'
        setProgress(prev => ({ ...prev, message: errMsg }))
        setTaskProgress('book-load', { title: 'Book Loader', status: 'error', message: errMsg })
        throw new Error('Start failed')
      }
    } catch (err) {
      setStatus('error')
      setTaskProgress('book-load', { title: 'Book Loader', status: 'error', message: err.message })
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

      setTaskProgress('book-load', { 
        title: `Indexing ${bookName.trim()}`, 
        status: data.status === 'done' ? 'done' : 'running', 
        progress: data.progress ?? 0, 
        total: data.total ?? 0, 
        message: data.message || '' 
      })

      if (data.status === 'done') {
        setStatus('done')
        onLoaded(data.characters || [], bookName.trim())
        es.close()
        setTimeout(() => clearTask('book-load'), 3000)
      } else if (data.status === 'error') {
        setStatus('error')
        setTaskProgress('book-load', { title: `Indexing ${bookName.trim()}`, status: 'error', message: data.message || 'Error occurred' })
        es.close()
      }
    }

    es.onerror = () => {
      setStatus('error')
      setTaskProgress('book-load', { title: `Indexing ${bookName.trim()}`, status: 'error', message: 'SSE Connection lost' })
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
          <p className="section-subtitle">Provide the book file path and name to begin indexing</p>
        </div>
      </div>

      {Object.keys(library).length > 0 && (
        <div className="form-group" style={{marginBottom: '1rem'}}>
          <label style={{display: 'inline-flex', alignItems: 'center', cursor: 'pointer'}}>
            <input 
              type="radio" 
              checked={useExisting} 
              onChange={() => {
                setUseExisting(true)
                const firstBook = Object.keys(library)[0]
                setBookName(firstBook)
                setBookPath(library[firstBook].book_path)
              }} 
              style={{marginRight: '8px'}}
              disabled={isLoading}
            />
            Select from Library
          </label>
          <label style={{marginLeft: '2rem', display: 'inline-flex', alignItems: 'center', cursor: 'pointer'}}>
            <input 
              type="radio" 
              checked={!useExisting} 
              onChange={() => {
                setUseExisting(false)
                setBookName('')
                setBookPath('')
              }} 
              style={{marginRight: '8px'}}
              disabled={isLoading}
            />
            Add New Book
          </label>
        </div>
      )}

      {useExisting ? (
        <div className="form-group" style={{marginBottom: '1rem'}}>
          <label htmlFor="book-select">Select Book</label>
          <select
            id="book-select"
            className="select"
            value={bookName}
            onChange={(e) => {
              const name = e.target.value
              setBookName(name)
              setBookPath(library[name]?.book_path || '')
            }}
            disabled={isLoading}
          >
            {Object.keys(library).map(name => (
              <option key={name} value={name}>{name}</option>
            ))}
          </select>
        </div>
      ) : (
        <div className="form-row">
          <div className="form-group">
            <label htmlFor="book-path">Book File Path</label>
            <input
              id="book-path"
              type="text"
              className="input"
              placeholder="e.g. data/EyeOfTheWorld/eyeoftheworld.txt"
              value={bookPath}
              onChange={(e) => setBookPath(e.target.value)}
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
      )}

      <button
        id="load-book-btn"
        className="btn btn-primary"
        onClick={handleLoad}
        disabled={!bookPath.trim() || !bookName.trim() || isLoading}
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
          ✗ {progress.message || 'Error loading book. Check the file path is correct and try again.'}
        </div>
      )}
    </section>
  )
}
