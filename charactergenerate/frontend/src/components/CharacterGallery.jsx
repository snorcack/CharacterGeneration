import { useState, useEffect } from 'react'
import { toast } from 'react-hot-toast'
import ConfirmModal from './ConfirmModal'
import { renderPromptBadge } from '../utils/badges'
import Lightbox from './Lightbox'

export default function CharacterGallery({ bookName, onEditCharacter, onSendPrompt, llmProvider, onDeleted }) {
  const [descriptions, setDescriptions] = useState({})
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  
  const [regenerating, setRegenerating] = useState({}) // { characterName: true }
  const [lightboxImg, setLightboxImg] = useState(null)
  
const [confirmConfig, setConfirmConfig] = useState({ isOpen: false })

function ImageCarousel({ images, charName, onOpenLightbox }) {
  const [idx, setIdx] = useState(0)
  if (!images || images.length === 0) {
    return (
      <div style={{width: '100%', aspectRatio: '1/1', background: 'rgba(0,0,0,0.2)', borderRadius: '8px', border: '1px solid var(--border)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: 'var(--text-faint)', marginBottom: '10px'}}>
        No Image
      </div>
    )
  }

  const next = (e) => { e.stopPropagation(); setIdx((idx + 1) % images.length) }
  const prev = (e) => { e.stopPropagation(); setIdx((idx - 1 + images.length) % images.length) }

  return (
    <div className="gallery-carousel" style={{width: '100%', aspectRatio: '1/1', marginBottom: '10px', overflow: 'hidden', borderRadius: '8px', border: '1px solid var(--border)'}}>
      <img 
        src={`/api/image/${images[idx]}`} 
        alt={charName} 
        style={{width: '100%', height: '100%', objectFit: 'cover', cursor: 'zoom-in'}} 
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

  const loadGallery = async () => {
    if (!bookName) return
    setLoading(true)
    setError(null)
    try {
      const res = await fetch(`/api/character-descriptions/${encodeURIComponent(bookName)}`)
      if (!res.ok) throw new Error('Failed to load gallery')
      const data = await res.json()
      setDescriptions(data.descriptions || {})
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    loadGallery()
  }, [bookName])

  const handleDelete = (charName, deletePromptsOnly) => {
    setConfirmConfig({
      isOpen: true,
      title: 'Confirm Deletion',
      message: `Are you sure you want to delete ${deletePromptsOnly ? 'prompts/images' : 'the entire description'} for ${charName}?`,
      destructive: true,
      onConfirm: async () => {
        setConfirmConfig({ isOpen: false })
        try {
      const res = await fetch('/api/delete-character-data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          book_name: bookName,
          character_name: charName,
          delete_prompts_only: deletePromptsOnly
        })
      })
      if (!res.ok) throw new Error('Failed to delete')
      loadGallery()
      if (onDeleted) onDeleted()
      toast.success(`${charName} data deleted.`)
    } catch (err) {
      toast.error('Error deleting: ' + err.message)
    }
      },
      onCancel: () => setConfirmConfig({ isOpen: false })
    })
  }

  const handleRegenerate = (charName) => {
    setConfirmConfig({
      isOpen: true,
      title: 'Regenerate Description',
      message: `Are you sure you want to regenerate the description for ${charName}? This will overwrite the existing one.`,
      destructive: false,
      onConfirm: async () => {
        setConfirmConfig({ isOpen: false })
        setRegenerating(prev => ({ ...prev, [charName]: true }))
    try {
      const res = await fetch('/api/character-details', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          character_name: charName,
          llm_provider: llmProvider || undefined,
          force_regenerate: true
        })
      })
      if (!res.ok) throw new Error('Failed to regenerate description')
      loadGallery()
      if (onDeleted) onDeleted() // To refresh carousel
      toast.success(`${charName} description regenerated.`)
    } catch (err) {
      toast.error('Error regenerating: ' + err.message)
    } finally {
      setRegenerating(prev => ({ ...prev, [charName]: false }))
    }
      },
      onCancel: () => setConfirmConfig({ isOpen: false })
    })
  }

  if (loading) return <div style={{padding: '20px', color: 'var(--text-faint)'}}>Loading gallery...</div>
  if (error) return <div style={{padding: '20px', color: 'var(--error)'}}>Error: {error}</div>

  const entries = Object.entries(descriptions)
  if (entries.length === 0) return <div style={{padding: '40px', textAlign: 'center', color: 'var(--text-faint)'}}>No characters saved in gallery yet.</div>

  return (
    <div style={{display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(600px, 1fr))', gap: '20px', padding: '10px'}}>
      <ConfirmModal {...confirmConfig} />
      <Lightbox src={lightboxImg} onClose={() => setLightboxImg(null)} />
      {entries.map(([charName, charData]) => (
        <div key={charName} className="glass-card" style={{padding: '24px', display: 'flex', gap: '24px', alignItems: 'flex-start', minHeight: '320px'}}>
          {/* Left side: Image carousel */}
          <div style={{width: '200px', flexShrink: 0, textAlign: 'center'}}>
            <ImageCarousel 
              images={charData.image_prompt_ids || (charData.image_prompt_id ? [charData.image_prompt_id] : [])} 
              charName={charName} 
              onOpenLightbox={setLightboxImg}
            />
            
            <div style={{display: 'flex', flexDirection: 'column', gap: '8px'}}>
              <button className="btn btn-secondary" onClick={() => onEditCharacter(charName)} style={{fontSize: '0.8rem', padding: '6px'}}>
                Edit in Studio
              </button>
            </div>
          </div>
          
          {/* Right side: details */}
          <div style={{flex: 1}}>
            <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '10px'}}>
              <h2 style={{margin: 0, color: 'var(--purple)'}}>{charName}</h2>
              <div style={{display: 'flex', gap: '8px'}}>
                <button 
                  className="btn btn-secondary" 
                  onClick={() => handleRegenerate(charName)} 
                  disabled={regenerating[charName]}
                  style={{fontSize: '0.75rem', padding: '4px 8px'}}
                  title="Regenerate Description"
                >
                  {regenerating[charName] ? '⏳...' : '🔄 Regenerate'}
                </button>
                <button 
                  className="btn btn-secondary" 
                  onClick={() => handleDelete(charName, true)}
                  style={{fontSize: '0.75rem', padding: '4px 8px'}}
                  title="Delete Prompts & Image"
                  disabled={!charData.prompts?.length && !charData.image_prompt_id}
                >
                  Clear Media
                </button>
                <button 
                  className="btn btn-secondary" 
                  onClick={() => handleDelete(charName, false)}
                  style={{fontSize: '0.75rem', padding: '4px 8px', color: '#ff6b6b', borderColor: 'rgba(255,107,107,0.3)'}}
                  title="Delete Entire Character Data"
                >
                  🗑️ Delete All
                </button>
              </div>
            </div>
            
            <div style={{fontSize: '0.9rem', color: 'var(--text-muted)', marginBottom: '15px', lineHeight: '1.5', maxHeight: '150px', overflowY: 'auto', background: 'rgba(0,0,0,0.1)', padding: '10px', borderRadius: '6px'}}>
              {charData.description || 'No description available.'}
            </div>
            
            {charData.prompts && charData.prompts.length > 0 && (
              <div>
                <h4 style={{margin: '0 0 8px 0', fontSize: '0.85rem', color: 'var(--text-faint)'}}>Saved Prompts ({charData.prompts.length})</h4>
                <div style={{display: 'flex', flexDirection: 'column', gap: '6px', maxHeight: '150px', overflowY: 'auto'}}>
                  {charData.prompts.map((p, i) => (
                    <div key={i} style={{fontSize: '0.8rem', padding: '8px', background: 'rgba(0,0,0,0.2)', border: '1px solid var(--border)', borderRadius: '6px'}}>
                      <div style={{marginBottom: '4px', display: 'flex', justifyContent: 'flex-end'}}>{renderPromptBadge(p)}</div>
                      {p}
                      <div style={{marginTop: '8px', display: 'flex', gap: '8px', opacity: 0.8}}>
                        <button 
                          className="btn btn-secondary" 
                          style={{fontSize: '0.65rem', padding: '4px 8px', flex: 1}}
                          onClick={(e) => { e.stopPropagation(); onSendPrompt && onSendPrompt(p, true); }}
                        >
                          🚀 Send to Image Gen
                        </button>
                        <button 
                          className="btn btn-secondary" 
                          style={{fontSize: '0.65rem', padding: '4px 8px', flex: 1}}
                          onClick={(e) => { e.stopPropagation(); onSendPrompt && onSendPrompt(p, false); }}
                        >
                          🎬 Send to Video Gen
                        </button>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        </div>
      ))}
    </div>
  )
}
