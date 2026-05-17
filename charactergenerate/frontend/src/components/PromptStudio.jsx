import { useState } from 'react'
import { Loader } from './Loader'
import { renderPromptBadge } from '../utils/badges'
import PromptEditor from './PromptEditor'

/**
 * PromptStudio — Section 04
 * Generate / Regenerate the Z-Image-Turbo prompt and provide a copy button.
 */
export default function PromptStudio({ 
  prompt, 
  setPrompt,
  savedPrompts = [],
  loading, 
  onGenerate, 
  onSave,
  canGenerate,
  gender,
  setGender,
  race,
  setRace,
  age,
  setAge
}) {
  const [copied, setCopied] = useState(false)

  const handleCopy = () => {
    if (!prompt) return
    navigator.clipboard.writeText(prompt).then(() => {
      setCopied(true)
      setTimeout(() => setCopied(false), 2200)
    })
  }

  return (
    <section className="glass-card animate-in">
      <div className="section-header">
        <span className="section-number">04</span>
        <div>
          <h2>Prompt Studio</h2>
          <p className="section-subtitle">
            Refine your image prompt and save your favorite versions
          </p>
        </div>
      </div>

      <div className="form-group" style={{ marginBottom: '24px' }}>
        <label style={{ color: 'var(--purple)', marginBottom: '12px' }}>
          Physical Overrides <span className="label-hint">(Swap character traits for the prompt)</span>
        </label>
        <div className="form-row" style={{ gridTemplateColumns: 'repeat(auto-fit, minmax(130px, 1fr))' }}>
          <input 
            type="text" 
            className="input" 
            value={gender} 
            onChange={e => setGender(e.target.value)}
            placeholder="Gender"
          />
          <input 
            type="text" 
            className="input" 
            value={race} 
            onChange={e => setRace(e.target.value)}
            placeholder="Race/Ethnicity"
          />
          <input 
            type="text" 
            className="input" 
            value={age} 
            onChange={e => setAge(e.target.value)}
            placeholder="Age"
          />
        </div>
      </div>

      <div style={{ display: 'flex', gap: '12px', flexWrap: 'wrap' }}>
        <button
          id="generate-prompt-btn"
          className="btn btn-primary generate-btn"
          style={{ flex: 1, minWidth: '140px' }}
          onClick={() => onGenerate('image')}
          disabled={!canGenerate || loading}
        >
          {loading ? (
            <><Loader small /> Generating…</>
          ) : prompt ? (
            '🔄 Regen Image'
          ) : (
            '✨ Image Prompt'
          )}
        </button>

        <button
          className="btn btn-primary generate-btn"
          style={{ flex: 1, minWidth: '140px' }}
          onClick={() => onGenerate('video')}
          disabled={!canGenerate || loading}
        >
          {loading ? (
            <><Loader small /> Generating…</>
          ) : prompt ? (
            '🔄 Regen Video'
          ) : (
            '🎥 Video Prompt'
          )}
        </button>

        {prompt && !loading && (
          <button
            className="btn btn-secondary"
            style={{ padding: '0 20px', borderColor: 'var(--success)', color: 'var(--success)' }}
            onClick={onSave}
            title="Save this prompt to character library"
          >
            💾 Save
          </button>
        )}
      </div>

      {loading && (
        <div className="loading-row" style={{ marginTop: 16 }}>
          <Loader />
          <span>Building your image prompt with the local LLM…</span>
        </div>
      )}

      {prompt && !loading && (
        <div className="prompt-output" style={{ marginTop: '24px' }}>
          <div className="prompt-output-header">
            <span>Editable Prompt</span>
            <button
              id="copy-prompt-btn"
              className={`btn-copy ${copied ? 'copied' : ''}`}
              onClick={handleCopy}
            >
              {copied ? '✓ Copied!' : '📋 Copy'}
            </button>
          </div>
          <div style={{ padding: '4px' }}>
            <PromptEditor 
              value={prompt}
              onChange={setPrompt}
              style={{ height: '200px' }}
            />
          </div>
        </div>
      )}

      {savedPrompts.length > 0 && (
        <div className="saved-prompts-section" style={{ marginTop: '24px' }}>
          <label style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: '8px', display: 'block' }}>
            SAVED PROMPTS ({savedPrompts.length})
          </label>
          <div className="saved-prompts-list" style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
            {savedPrompts.map((p, idx) => (
              <div 
                key={idx} 
                className={`saved-prompt-item ${p === prompt ? 'active' : ''}`}
                onClick={() => setPrompt(p)}
                style={{
                  padding: '10px 12px',
                  background: 'rgba(255,255,255,0.03)',
                  border: `1px solid ${p === prompt ? 'var(--purple)' : 'var(--border)'}`,
                  borderRadius: '8px',
                  fontSize: '0.8rem',
                  cursor: 'pointer',
                  color: p === prompt ? 'var(--text)' : 'var(--text-muted)',
                  display: '-webkit-box',
                  WebkitLineClamp: '2',
                  WebkitBoxOrient: 'vertical',
                  overflow: 'hidden',
                  textOverflow: 'ellipsis',
                  transition: 'all 0.2s',
                  lineHeight: '1.4'
                }}
              >
                <div style={{display: 'flex', justifyContent: 'flex-end', marginBottom: '4px'}}>
                  {renderPromptBadge(p)}
                </div>
                {p}
              </div>
            ))}
          </div>
        </div>
      )}
    </section>
  )
}
