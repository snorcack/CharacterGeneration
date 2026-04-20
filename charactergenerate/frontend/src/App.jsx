import { useState, useCallback } from 'react'
import BookLoader from './components/BookLoader'
import CharacterPanel from './components/CharacterPanel'
import ScenarioSelector from './components/ScenarioSelector'
import PromptStudio from './components/PromptStudio'
import ComfyPanel from './components/ComfyPanel'
import ComfyDebugger from './components/ComfyDebugger'

/**
 * App — root state manager.
 * Owns all shared state and passes handlers + data down to each section.
 * Sections reveal progressively as each stage completes.
 */
export default function App() {
  const [view, setView] = useState('main') // main | debug

  // ── Book loading ──────────────────────────────────────────────
  const [bookStatus, setBookStatus] = useState('idle') // idle | loading | done | error
  const [progress, setProgress] = useState({ stage: '', progress: 0, total: 0, message: '' })
  const [characters, setCharacters] = useState([])

  // ── Character selection ───────────────────────────────────────
  const [selectedCharacter, setSelectedCharacter] = useState('')
  const [charDetailsLoading, setCharDetailsLoading] = useState(false)
  const [charDetails, setCharDetails] = useState(null)   // { description, scenarios }
  const [description, setDescription] = useState('')     // user-editable

  // ── Casting / Adaptation parameters ──────────────────────────
  const [industry, setIndustry] = useState('hollywood')
  const [genre, setGenre] = useState('')                 // e.g. "Cyberpunk", "Victorian"
  const [decade, setDecade] = useState('2026')           // e.g. "1950", "1980"
  const [actorName, setActorName] = useState('')         // user-editable override
  const [actorLoading, setActorLoading] = useState(false)

  // ── Physical Overrides ────────────────────────────────────────
  const [gender, setGender] = useState('')
  const [race, setRace] = useState('')
  const [age, setAge] = useState('')

  // ── Scenario / prompt ─────────────────────────────────────────
  const [selectedScenario, setSelectedScenario] = useState(null) // { label, context }
  const [prompt, setPrompt] = useState('')
  const [promptLoading, setPromptLoading] = useState(false)

  // ── History ───────────────────────────────────────────────────
  const [promptHistory, setPromptHistory] = useState([]) // Array of { prompt, id, char, genre }

  // ── Handlers ──────────────────────────────────────────────────

  /** Called by BookLoader once the SSE stream signals completion. */
  const handleBookLoaded = useCallback((chars) => {
    setCharacters(chars)
    // Reset downstream state
    setSelectedCharacter('')
    setCharDetails(null)
    setDescription('')
    setActorName('')
    setSelectedScenario(null)
    setPrompt('')
    setGender('')
    setRace('')
    setAge('')
  }, [])

  /** Called when user changes the character dropdown. */
  const handleCharacterSelect = useCallback(async (charName) => {
    setSelectedCharacter(charName)
    setCharDetails(null)
    setDescription('')
    setActorName('')
    setSelectedScenario(null)
    setPrompt('')
    setGender('')
    setRace('')
    setAge('')

    if (!charName) return

    setCharDetailsLoading(true)
    try {
      const res = await fetch('/api/character-details', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ character_name: charName }),
      })
      if (!res.ok) throw new Error(await res.text())
      const data = await res.json()
      setCharDetails(data)
      setDescription(data.description)
    } catch (err) {
      console.error('character-details error:', err)
    } finally {
      setCharDetailsLoading(false)
    }
  }, [])

  /** Cast an actor for the current character + description + industry. */
  const handleCastActor = useCallback(async () => {
    setActorLoading(true)
    try {
      const res = await fetch('/api/cast-actor', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          character_name: selectedCharacter,
          description,
          industry,
          genre,
          decade
        }),
      })
      if (!res.ok) throw new Error(await res.text())
      const data = await res.json()
      setActorName(data.actor_name)
    } catch (err) {
      console.error('cast-actor error:', err)
    } finally {
      setActorLoading(false)
    }
  }, [selectedCharacter, description, industry, genre, decade])

  /** Generate the final image prompt with user-edited description + actor. */
  const handleGeneratePrompt = useCallback(async () => {
    if (!selectedScenario) return
    setPromptLoading(true)
    try {
      const res = await fetch('/api/generate-prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          character_name: selectedCharacter,
          description,
          scenario_context: selectedScenario.context,
          actor_name: actorName,
          genre,
          decade,
          gender,
          race,
          age
        }),
      })
      if (!res.ok) throw new Error(await res.text())
      const data = await res.json()
      setPrompt(data.prompt)
      
      // Save to history
      const historyItem = {
        id: Date.now(),
        prompt: data.prompt,
        char: selectedCharacter,
        genre: genre || 'Standard',
        scenario: selectedScenario.label,
        timestamp: new Date().toLocaleTimeString()
      }
      setPromptHistory(prev => [historyItem, ...prev])

    } catch (err) {
      console.error('generate-prompt error:', err)
    } finally {
      setPromptLoading(false)
    }
  }, [selectedCharacter, description, selectedScenario, actorName, genre, decade, gender, race, age])

  // ── Render ────────────────────────────────────────────────────
  return (
    <div className={`app ${view === 'main' ? 'app-dashboard' : ''}`}>
      <header className="header">
        <div className="header-content" style={{width: '100%'}}>
          <div className="header-icon">{view === 'main' ? '📖' : '🛠️'}</div>
          <div style={{flex: 1}}>
            <h1>{view === 'main' ? 'Character Portrait Generator' : 'ComfyUI Debugger'}</h1>
            <p>{view === 'main' ? 'From book to image prompt — powered by RAG & local LLM' : 'Diagnostics and workflow testing'}</p>
          </div>
          <button 
            className="btn btn-secondary" 
            onClick={() => setView(view === 'main' ? 'debug' : 'main')}
            style={{fontSize: '0.8rem', padding: '8px 16px'}}
          >
            {view === 'main' ? '🔧 Debug Mode' : '◀ Back to App'}
          </button>
        </div>
      </header>

      <main className={view === 'main' ? 'dashboard animate-in' : 'main'}>
        {view === 'debug' ? (
          <ComfyDebugger />
        ) : (
          <>
            {/* Sidebar Left: Loading & Characters */}
            <div className="dashboard-left">
              <BookLoader
                status={bookStatus}
                setStatus={setBookStatus}
                progress={progress}
                setProgress={setProgress}
                onLoaded={handleBookLoaded}
              />
              
              {bookStatus === 'done' && (
                <div className="glass-card" style={{padding: '20px'}}>
                  <div className="section-header" style={{marginBottom: '16px'}}>
                    <h2 style={{fontSize: '1rem'}}>Active Character</h2>
                  </div>
                  <div className="select-wrapper">
                    <select
                      id="character-select"
                      className="select"
                      value={selectedCharacter}
                      onChange={(e) => handleCharacterSelect(e.target.value)}
                      disabled={charDetailsLoading}
                    >
                      <option value="">— Choose —</option>
                      {characters.map((c) => (
                        <option key={c} value={c}>{c}</option>
                      ))}
                    </select>
                  </div>
                </div>
              )}
            </div>

            {/* Main Center: Details, Scenarios, Prompting */}
            <div className="dashboard-main">
              {bookStatus === 'done' && selectedCharacter && (
                <>
                  <CharacterPanel
                    characters={characters}
                    selectedCharacter={selectedCharacter}
                    onSelectCharacter={handleCharacterSelect}
                    charDetailsLoading={charDetailsLoading}
                    description={description}
                    setDescription={setDescription}
                    industry={industry}
                    setIndustry={setIndustry}
                    genre={genre}
                    setGenre={setGenre}
                    decade={decade}
                    setDecade={setDecade}
                    actorName={actorName}
                    setActorName={setActorName}
                    actorLoading={actorLoading}
                    onCastActor={handleCastActor}
                    minimal={true} // New prop for simpler UI if needed
                  />

                  {charDetails && !charDetailsLoading && (
                    <ScenarioSelector
                      scenarios={charDetails.scenarios}
                      selectedScenario={selectedScenario}
                      onSelectScenario={(s) => {
                        setSelectedScenario(s)
                        setPrompt('')
                      }}
                    />
                  )}

                  {selectedScenario && (
                    <PromptStudio
                      prompt={prompt}
                      loading={promptLoading}
                      onGenerate={handleGeneratePrompt}
                      canGenerate={!!(selectedCharacter && selectedScenario)}
                      gender={gender}
                      setGender={setGender}
                      race={race}
                      setRace={setRace}
                      age={age}
                      setAge={setAge}
                    />
                  )}
                </>
              )}
              {(!selectedCharacter && bookStatus === 'done') && (
                <div className="glass-card" style={{textAlign: 'center', padding: '100px 40px', color: 'var(--text-faint)'}}>
                  <div style={{fontSize: '3rem', marginBottom: '20px'}}>👤</div>
                  <p>Select a character from the sidebar to begin portrait generation</p>
                </div>
              )}
            </div>

            {/* Sidebar Right: Prompt History & ComfyUI */}
            <div className="dashboard-right">
              {/* ComfyUI Section — Always Visible */}
              <ComfyPanel prompt={prompt} />

              {/* Prompt History */}
              {promptHistory.length > 0 && (
                <div className="glass-card animate-in" style={{padding: '20px'}}>
                   <div className="section-header" style={{marginBottom: '16px'}}>
                    <div className="section-number">HIST</div>
                    <h2 style={{fontSize: '0.95rem'}}>Prompt History</h2>
                  </div>
                  <div className="history-list" style={{display: 'flex', flexDirection: 'column', gap: '10px', maxH: '400px', overflowY: 'auto'}}>
                    {promptHistory.map(item => (
                      <div 
                        key={item.id} 
                        className="history-item"
                        onClick={() => setPrompt(item.prompt)}
                        style={{
                          background: prompt === item.prompt ? 'var(--purple-glow)' : 'rgba(0,0,0,0.2)',
                          border: `1px solid ${prompt === item.prompt ? 'var(--purple)' : 'var(--border)'}`,
                          borderRadius: '8px',
                          padding: '10px',
                          cursor: 'pointer',
                          fontSize: '0.75rem',
                          transition: 'all 0.2s'
                        }}
                      >
                        <div style={{display: 'flex', justifyContent: 'space-between', marginBottom: '4px'}}>
                          <span style={{fontWeight: '700', color: 'var(--purple)'}}>{item.char}</span>
                          <span style={{color: 'var(--text-faint)'}}>{item.timestamp}</span>
                        </div>
                        <div style={{color: 'var(--text-muted)', fontSize: '0.7rem'}}>{item.genre} | {item.scenario}</div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          </>
        )}
      </main>
    </div>
  )
}
