import { useState } from 'react'
import { Loader } from './Loader'

/**
 * PromptStudio — Section 04
 * Generate / Regenerate the Z-Image-Turbo prompt and provide a copy button.
 */
export default function PromptStudio({ 
  prompt, 
  loading, 
  onGenerate, 
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
            Generate your Z-Image-Turbo / Stable Diffusion character portrait prompt
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

      <button
        id="generate-prompt-btn"
        className="btn btn-primary generate-btn"
        onClick={onGenerate}
        disabled={!canGenerate || loading}
      >
        {loading ? (
          <><Loader small /> Generating…</>
        ) : prompt ? (
          '🔄 Regenerate Prompt'
        ) : (
          '✨ Generate Prompt'
        )}
      </button>

      {loading && (
        <div className="loading-row" style={{ marginTop: 16 }}>
          <Loader />
          <span>Building your image prompt with the local LLM…</span>
        </div>
      )}

      {prompt && !loading && (
        <div className="prompt-output">
          <div className="prompt-output-header">
            <span>Generated Prompt</span>
            <button
              id="copy-prompt-btn"
              className={`btn-copy ${copied ? 'copied' : ''}`}
              onClick={handleCopy}
            >
              {copied ? '✓ Copied!' : '📋 Copy'}
            </button>
          </div>
          <div className="prompt-text">{prompt}</div>
        </div>
      )}
    </section>
  )
}
