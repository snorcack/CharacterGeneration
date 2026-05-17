import { useState, useEffect } from 'react'
import { Loader } from './Loader'
import { toast } from 'react-hot-toast'
import { useTasks } from '../context/TaskContext'
import PromptEditor from './PromptEditor'

export default function GroupSceneFinder({ characters = [], onSelectScenario, onSendPrompt, llmProvider, onAgentDone, initiallyOpen = false }) {
  const [selectedChars, setSelectedChars] = useState([])
  const [loading, setLoading] = useState(false)
  const [scenes, setScenes] = useState([])
  const [message, setMessage] = useState('')
  const [isOpen, setIsOpen] = useState(initiallyOpen)
  const { setTaskProgress, clearTask } = useTasks()
  
  const [groupPrompts, setGroupPrompts] = useState({}) // { [idx]: { imagePrompt: '', videoPrompt: '', loading: false } }

  // Agent State
  const [agentLoading, setAgentLoading] = useState(false)
  const [agentStatus, setAgentStatus] = useState({ status: 'idle', message: '', progress: 0, total: 0 })

  // Agent Config
  const [useCasting, setUseCasting] = useState(false)
  const [agentGenre, setAgentGenre] = useState('')
  const [agentDecade, setAgentDecade] = useState('2026')
  const [agentIndustry, setAgentIndustry] = useState('hollywood')

  useEffect(() => {
    let eventSource = null
    if (agentLoading) {
      eventSource = new EventSource('/api/agent-status')
      eventSource.onmessage = (event) => {
        const data = JSON.parse(event.data)
        setAgentStatus(data)
        setTaskProgress('agent-analysis', { 
          title: 'Character Analysis Agent', 
          status: data.status === 'done' ? 'done' : 'running', 
          progress: data.progress, 
          total: data.total, 
          message: data.message 
        })
        
        if (data.status === 'done' || data.status === 'error') {
          setAgentLoading(false)
          eventSource.close()
          if (data.status === 'error') {
            setTaskProgress('agent-analysis', { title: 'Character Analysis Agent', status: 'error', message: data.message || 'Agent error' })
          } else {
            setTimeout(() => clearTask('agent-analysis'), 3000)
          }
          if (data.status === 'done' && onAgentDone) {
            onAgentDone()
          }
        }
      }
      eventSource.onerror = () => {
        setAgentLoading(false)
        setTaskProgress('agent-analysis', { title: 'Character Analysis Agent', status: 'error', message: 'SSE Connection lost' })
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

  const handleFindScenes = async () => {
    if (selectedChars.length < 2) {
      toast.error('Please select at least 2 characters to find shared scenes.')
      return
    }
    setLoading(true)
    setMessage('')
    setScenes([])
    try {
      const res = await fetch('/api/find-group-scenes', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          character_names: selectedChars,
          llm_provider: llmProvider || undefined
        })
      })
      const data = await res.json()
      if (data.scenes && data.scenes.length > 0) {
        setScenes(data.scenes)
      } else {
        setMessage(data.message || 'No scenes found.')
      }
    } catch (err) {
      console.error(err)
      setMessage('Error searching for scenes.')
    } finally {
      setLoading(false)
    }
  }

  const handleAnalyzeCharacters = async () => {
    if (selectedChars.length === 0) {
      toast.error('Please select at least 1 character to analyze.')
      return
    }
    setAgentLoading(true)
    setAgentStatus({ status: 'running', message: 'Starting agent...', progress: 0, total: selectedChars.length })
    try {
      const res = await fetch('/api/batch-analyze-characters', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          character_names: selectedChars,
          use_casting: useCasting,
          genre: agentGenre,
          decade: agentDecade,
          industry: agentIndustry,
          llm_provider: llmProvider || undefined
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
    if (!confirm('Are you sure you want to abort the character analysis?')) return
    try {
      const res = await fetch('/api/abort-agent', { method: 'POST' })
      if (!res.ok) throw new Error('Failed to abort')
      toast.success('Abort requested...')
    } catch (err) {
      console.error(err)
      toast.error('Failed to abort: ' + err.message)
    }
  }

  const handleGenerateGroupPrompt = async (scene, idx) => {
    setGroupPrompts(prev => ({ ...prev, [idx]: { ...prev[idx], loading: true } }))
    try {
      const res = await fetch('/api/generate-group-prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          character_names: selectedChars,
          scenario_context: scene.context,
          genre: agentGenre,
          llm_provider: llmProvider || undefined
        })
      })
      if (!res.ok) throw new Error('Failed to generate group prompts')
      const data = await res.json()
      setGroupPrompts(prev => ({ 
        ...prev, 
        [idx]: { imagePrompt: data.image_prompt, videoPrompt: data.video_prompt, loading: false } 
      }))
      toast.success('Group prompts generated successfully!')
    } catch (err) {
      toast.error('Generation failed: ' + err.message)
      setGroupPrompts(prev => ({ ...prev, [idx]: { ...prev[idx], loading: false } }))
    }
  }

  return (
    <div className="group-scene-finder glass-card animate-in" style={{ marginTop: '20px' }}>
      <button 
        className="btn btn-secondary" 
        style={{ width: '100%', justifyContent: 'space-between' }}
        onClick={() => setIsOpen(!isOpen)}
      >
        <span>🔍 Multi-Character Agent</span>
        <span>{isOpen ? '▲' : '▼'}</span>
      </button>

      {isOpen && (
        <div style={{ marginTop: '16px' }}>
          <p className="section-subtitle" style={{ marginBottom: '12px' }}>
            Select characters to find shared scenes or batch-generate their descriptions and prompts.
          </p>

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
            {characters.map(char => (
              <label key={char} style={{ 
                display: 'flex', 
                alignItems: 'center', 
                gap: '8px', 
                fontSize: '0.85rem', 
                cursor: 'pointer',
                color: selectedChars.includes(char) ? 'var(--purple)' : 'var(--text-muted)'
              }}>
                <input 
                  type="checkbox" 
                  checked={selectedChars.includes(char)}
                  onChange={() => toggleChar(char)}
                  style={{ accentColor: 'var(--purple)' }}
                />
                {char}
              </label>
            ))}
          </div>

          <div className="agent-config-grid" style={{ 
            display: 'grid', 
            gridTemplateColumns: '1fr 1fr', 
            gap: '10px', 
            marginBottom: '16px',
            padding: '12px',
            background: 'rgba(255,255,255,0.03)',
            borderRadius: '8px',
            border: '1px solid var(--border)'
          }}>
            <div style={{ gridColumn: 'span 2' }}>
              <label style={{ display: 'flex', alignItems: 'center', gap: '8px', fontSize: '0.8rem', cursor: 'pointer' }}>
                <input type="checkbox" checked={useCasting} onChange={e => setUseCasting(e.target.checked)} style={{ accentColor: 'var(--purple)' }} />
                <span>Auto-Cast Actors (AI Casting)</span>
              </label>
            </div>
            
            <div>
              <label style={{ fontSize: '0.7rem', color: 'var(--text-faint)', display: 'block', marginBottom: '4px' }}>GENRE</label>
              <input 
                type="text" 
                className="input" 
                style={{ fontSize: '0.8rem', padding: '6px' }} 
                placeholder="e.g. Cyberpunk" 
                value={agentGenre}
                onChange={e => setAgentGenre(e.target.value)}
              />
            </div>
            
            <div>
              <label style={{ fontSize: '0.7rem', color: 'var(--text-faint)', display: 'block', marginBottom: '4px' }}>DECADE</label>
              <input 
                type="text" 
                className="input" 
                style={{ fontSize: '0.8rem', padding: '6px' }} 
                placeholder="e.g. 1980" 
                value={agentDecade}
                onChange={e => setAgentDecade(e.target.value)}
              />
            </div>

            <div style={{ gridColumn: 'span 2' }}>
              <label style={{ fontSize: '0.7rem', color: 'var(--text-faint)', display: 'block', marginBottom: '4px' }}>CASTING INDUSTRY</label>
              <select 
                className="select" 
                style={{ fontSize: '0.8rem', padding: '6px' }}
                value={agentIndustry}
                onChange={e => setAgentIndustry(e.target.value)}
              >
                <option value="hollywood">Hollywood</option>
                <option value="bollywood">Bollywood</option>
                <option value="british">British Cinema</option>
                <option value="anime">Anime (Voice Actor)</option>
              </select>
            </div>
          </div>

          <div style={{ display: 'flex', gap: '8px', marginBottom: '16px' }}>
            <button 
              className="btn btn-primary" 
              style={{ flex: 1 }}
              onClick={handleFindScenes}
              disabled={loading || selectedChars.length < 2 || agentLoading}
            >
              {loading ? <Loader small /> : 'Find Shared Scenes'}
            </button>
            <button 
              className="btn btn-secondary" 
              style={{ flex: 1, border: '1px solid var(--purple)' }}
              onClick={handleAnalyzeCharacters}
              disabled={agentLoading || loading || selectedChars.length === 0}
            >
              {agentLoading ? <Loader small /> : 'Analyze & Save'}
            </button>
          </div>

          {(agentLoading || agentStatus.status !== 'idle') && (
            <div className="agent-progress-box" style={{ 
              padding: '12px', 
              background: 'rgba(168, 85, 247, 0.05)', 
              border: '1px solid rgba(168, 85, 247, 0.2)',
              borderRadius: '8px',
              marginBottom: '16px'
            }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.8rem', marginBottom: '8px' }}>
                <span style={{ color: 'var(--purple)', fontWeight: '600' }}>
                  {agentStatus.status === 'running' ? 'Agent Processing...' : 
                   agentStatus.status === 'done' ? 'Analysis Complete' : 
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
                  🛑 Abort Analysis
                </button>
              )}

              <div className="progress-bar-bg" style={{ height: '6px', background: 'rgba(0,0,0,0.2)', borderRadius: '3px', overflow: 'hidden' }}>
                <div 
                  className="progress-bar-fill" 
                  style={{ 
                    height: '100%', 
                    background: 'var(--purple)', 
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

          {loading && (
            <div className="loading-row" style={{ marginTop: '16px', marginBottom: '16px' }}>
              <Loader />
              <span>Scanning the book for character interactions...</span>
            </div>
          )}

          {message && (
            <div style={{ 
              marginTop: '16px', 
              padding: '12px', 
              background: 'rgba(245,158,11,0.1)', 
              border: '1px solid rgba(245,158,11,0.2)',
              borderRadius: '8px',
              color: 'var(--warning)',
              fontSize: '0.9rem',
              textAlign: 'center'
            }}>
              {message}
            </div>
          )}

          {scenes.length > 0 && (
            <div className="group-scenes-list" style={{ marginTop: '20px' }}>
              <label style={{ fontSize: '0.75rem', color: 'var(--text-muted)', marginBottom: '8px', display: 'block' }}>
                FOUND SCENES ({scenes.length})
              </label>
              <div style={{ display: 'flex', flexDirection: 'column', gap: '10px' }}>
                {scenes.map((s, idx) => (
                  <div 
                    key={idx} 
                    className="scenario-card"
                    style={{ padding: '12px', cursor: 'default' }}
                  >
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '4px' }}>
                      <div style={{ fontWeight: '600', fontSize: '0.9rem', color: 'var(--purple)' }}>
                        Scene {idx + 1}
                      </div>
                      <button 
                        className="btn btn-secondary" 
                        style={{ fontSize: '0.7rem', padding: '4px 8px' }}
                        onClick={() => {
                          onSelectScenario(s)
                          toast.success('Scene sent to Studio! Make sure to select a character.')
                        }}
                        title="Send this scene context to the active character in Character Studio"
                      >
                        Use Context
                      </button>
                    </div>
                    <div style={{ fontSize: '0.85rem', marginBottom: '10px' }}>{s.label}</div>
                    
                    <button 
                      className="btn btn-primary" 
                      style={{ fontSize: '0.75rem', padding: '6px 12px', width: '100%' }}
                      onClick={() => handleGenerateGroupPrompt(s, idx)}
                      disabled={groupPrompts[idx]?.loading}
                    >
                      {groupPrompts[idx]?.loading ? <><Loader small /> Generating...</> : '✨ Generate Group Media Prompts'}
                    </button>
                    
                    {groupPrompts[idx] && !groupPrompts[idx].loading && groupPrompts[idx].imagePrompt && (
                      <div className="animate-in" style={{ marginTop: '12px', display: 'flex', flexDirection: 'column', gap: '10px' }}>
                        <div>
                          <label style={{ fontSize: '0.7rem', color: 'var(--text-faint)', marginBottom: '4px', display: 'flex', justifyContent: 'space-between' }}>
                            <span>IMAGE PROMPT</span>
                            <button 
                              className="btn btn-secondary" 
                              style={{ fontSize: '0.65rem', padding: '2px 8px', height: 'auto' }}
                              onClick={() => onSendPrompt && onSendPrompt(groupPrompts[idx].imagePrompt, true)}
                            >
                              🚀 Send to Gen
                            </button>
                          </label>
                          <div style={{ background: 'rgba(0,0,0,0.2)', border: '1px solid var(--border)', borderRadius: '8px', padding: '4px' }}>
                            <PromptEditor 
                              value={groupPrompts[idx].imagePrompt}
                              onChange={() => {}}
                              readOnly={true}
                              style={{ height: '120px' }}
                            />
                          </div>
                        </div>
                        <div>
                          <label style={{ fontSize: '0.7rem', color: 'var(--text-faint)', marginBottom: '4px', display: 'flex', justifyContent: 'space-between' }}>
                            <span>VIDEO PROMPT (LTX)</span>
                            <button 
                              className="btn btn-secondary" 
                              style={{ fontSize: '0.65rem', padding: '2px 8px', height: 'auto' }}
                              onClick={() => onSendPrompt && onSendPrompt(groupPrompts[idx].videoPrompt, false)}
                            >
                              🎬 Send to Gen
                            </button>
                          </label>
                          <div style={{ background: 'rgba(0,0,0,0.2)', border: '1px solid var(--border)', borderRadius: '8px', padding: '4px' }}>
                            <PromptEditor 
                              value={groupPrompts[idx].videoPrompt}
                              onChange={() => {}}
                              readOnly={true}
                              style={{ height: '120px' }}
                            />
                          </div>
                        </div>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          )}
        </div>
      )}
    </div>
  )
}
