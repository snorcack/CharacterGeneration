import { useState, useCallback, useRef } from 'react'
import BookLoader from './components/BookLoader'
import CharacterPanel from './components/CharacterPanel'
import ScenarioSelector from './components/ScenarioSelector'
import PromptStudio from './components/PromptStudio'
import ComfyPanel from './components/ComfyPanel'
import ComfyDebugger from './components/ComfyDebugger'
import DescriptionCarousel from './components/DescriptionCarousel'
import GroupSceneFinder from './components/GroupSceneFinder'
import BatchImageGenerator from './components/BatchImageGenerator'
import CharacterGallery from './components/CharacterGallery'
import LocationsPanel from './components/LocationsPanel'
import { Toaster, toast } from 'react-hot-toast'
import { renderPromptBadge } from './utils/badges'

/**
 * App — root state manager.
 * Owns all shared state and passes handlers + data down to each section.
 * Sections reveal progressively as each stage completes.
 */
export default function App() {
  const [view, setView] = useState('main') // main | debug
  const [activeTab, setActiveTab] = useState('generator') // generator | agents
  const [llmProvider, setLlmProvider] = useState('') // '' means use backend default

  // ── Book loading ──────────────────────────────────────────────
  const [bookStatus, setBookStatus] = useState('idle') // idle | loading | done | error
  const [progress, setProgress] = useState({ stage: '', progress: 0, total: 0, message: '' })
  const [characters, setCharacters] = useState([])

  // ── Character selection ───────────────────────────────────────
  const [selectedCharacter, setSelectedCharacter] = useState('')
  const [customCharInput, setCustomCharInput] = useState('')
  const [charDetailsLoading, setCharDetailsLoading] = useState(false)
  const [charError, setCharError] = useState('')
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
  const [savedPrompts, setSavedPrompts] = useState([])
  const [promptLoading, setPromptLoading] = useState(false)

  // ── History ───────────────────────────────────────────────
  const [promptHistory, setPromptHistory] = useState([]) // Array of { prompt, id, char, genre }

  const comfyRef = useRef(null)

  const handleSendToGen = useCallback((promptText, autoGenerate = false) => {
    setPrompt(promptText)
    toast.success(autoGenerate ? 'Generating image...' : 'Prompt sent to Studio!')
    if (activeTab !== 'generator') setActiveTab('generator')
    if (autoGenerate) {
      setTimeout(() => {
        comfyRef.current?.triggerGeneration()
      }, 200)
    }
  }, [activeTab])

  // ── Carousel refresh ──────────────────────────────────────
  const [carouselRefresh, setCarouselRefresh] = useState(0)

  // ── UI State ────────────────────────────────────────────────
  const [leftCollapsed, setLeftCollapsed] = useState(false)
  const [rightCollapsed, setRightCollapsed] = useState(false)
  const [currentBookName, setCurrentBookName] = useState('')

  // ── Handlers ──────────────────────────────────────────────────

  /** Called by BookLoader once the SSE stream signals completion. */
  const handleBookLoaded = useCallback((chars, bookName) => {
    setCharacters(chars)
    setCurrentBookName(bookName || '')
    // Reset downstream state
    setSelectedCharacter('')
    setCustomCharInput('')
    setCharError('')
    setCharDetails(null)
    setDescription('')
    setActorName('')
    setSelectedScenario(null)
    setPrompt('')
    setSavedPrompts([])
    setGender('')
    setRace('')
    setAge('')
    // Refresh carousel to load any pre-existing cached descriptions
    setCarouselRefresh(t => t + 1)
  }, [])

  /** Called when user changes the character dropdown or clicks a carousel card. */
  const handleCharacterSelect = useCallback(async (charName, cachedEntry = null) => {
    setSelectedCharacter(charName)
    setCustomCharInput(charName)
    setCharError('')
    setCharDetails(null)
    setDescription('')
    setActorName('')
    setSelectedScenario(null)
    setPrompt('')
    setSavedPrompts([])
    setGender('')
    setRace('')
    setAge('')

    if (!charName) return

    // If caller already has the cached entry, use it directly — no API call needed
    if (cachedEntry && cachedEntry.description) {
      setCharDetails({ description: cachedEntry.description, scenarios: cachedEntry.scenarios || [] })
      setDescription(cachedEntry.description)
      setSavedPrompts(cachedEntry.prompts || [])
      return
    }

    setCharDetailsLoading(true)
    try {
      const res = await fetch('/api/character-details', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ character_name: charName, llm_provider: llmProvider || undefined }),
      })
      if (!res.ok) {
        const errorData = await res.json().catch(() => ({}))
        throw new Error(errorData.detail || await res.text())
      }
      const data = await res.json()
      setCharDetails(data)
      setDescription(data.description)
      setSavedPrompts(data.prompts || [])
      // If this was freshly generated (not cached), bump carousel so the new card appears
      if (!data.cached) setCarouselRefresh(t => t + 1)
    } catch (err) {
      console.error('character-details error:', err)
      setCharError(err.message)
      toast.error('Error fetching details: ' + err.message)
    } finally {
      setCharDetailsLoading(false)
    }
  }, [llmProvider])

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
          decade,
          llm_provider: llmProvider || undefined
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

  /** Generate the final image/video prompt with user-edited description + actor. */
  const handleGeneratePrompt = useCallback(async (promptType = 'image') => {
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
          age,
          prompt_type: promptType,
          llm_provider: llmProvider || undefined
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

      toast.success('Prompt generated!')
    } catch (err) {
      console.error('generate-prompt error:', err)
      toast.error('Prompt generation failed: ' + err.message)
    } finally {
      setPromptLoading(false)
    }
  }, [selectedCharacter, description, selectedScenario, actorName, genre, decade, gender, race, age])
  
  /** Save the current prompt to the character's library entry. */
  const handleSavePrompt = useCallback(async () => {
    if (!prompt || !selectedCharacter || !currentBookName) return
    try {
      const res = await fetch('/api/save-prompt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          book_name: currentBookName,
          character_name: selectedCharacter,
          prompt: prompt
        }),
      })
      if (!res.ok) throw new Error(await res.text())
      const data = await res.json()
      setSavedPrompts(data.prompts)
      toast.success('Prompt saved successfully!')
    } catch (err) {
      console.error('save-prompt error:', err)
      toast.error('Failed to save prompt: ' + err.message)
    }
  }, [prompt, selectedCharacter, currentBookName])

  // ── Render ────────────────────────────────────────────────────
  return (
    <div className={`app ${view === 'main' ? 'app-dashboard' : ''}`}>
      <Toaster position="bottom-right" toastOptions={{ style: { background: '#333', color: '#fff', border: '1px solid var(--border)' } }} />
      <header className="header">
        <div className="header-content" style={{width: '100%'}}>
          <div className="header-icon">{view === 'main' ? '📖' : '🛠️'}</div>
          <div style={{flex: 1}}>
            <h1>{view === 'main' ? 'Character Portrait Generator' : 'ComfyUI Debugger'}</h1>
            <p>{view === 'main' ? 'From book to image prompt — powered by RAG & local LLM' : 'Diagnostics and workflow testing'}</p>
          </div>
          <div style={{display: 'flex', gap: '15px', alignItems: 'center'}}>
            <select 
              className="select" 
              style={{padding: '6px 12px', fontSize: '0.85rem', width: 'auto'}} 
              value={llmProvider} 
              onChange={e => setLlmProvider(e.target.value)}
              title="Text Generation Provider"
            >
              <option value="">Text LLM: Default (.env)</option>
              <option value="ollama">Text LLM: Ollama</option>
              <option value="openai">Text LLM: OpenAI</option>
              <option value="anthropic">Text LLM: Anthropic</option>
              <option value="gemini">Text LLM: Gemini</option>
            </select>
            <button 
              className="btn btn-secondary" 
              onClick={() => setView(view === 'main' ? 'debug' : 'main')}
              style={{fontSize: '0.8rem', padding: '8px 16px'}}
            >
              {view === 'main' ? '🔧 Debug Mode' : '◀ Back to App'}
            </button>
          </div>
        </div>
      </header>

      <main className={view === 'main' ? 'dashboard animate-in' : 'main'} style={{
        '--left-w': leftCollapsed ? '60px' : '320px',
        '--right-w': rightCollapsed ? '60px' : '340px'
      }}>
        {view === 'debug' ? (
          <ComfyDebugger />
        ) : (
          <>
            {/* Sidebar Left: Loading & Characters */}
            <div className={`dashboard-left ${leftCollapsed ? 'collapsed' : ''}`}>
              {leftCollapsed ? (
                <div className="glass-card collapsed-content" style={{height: '100%', cursor: 'pointer'}} onClick={() => setLeftCollapsed(false)}>
                  <button className="sidebar-toggle-btn">▶</button>
                  <div className="collapsed-text">CHARACTERS</div>
                </div>
              ) : (
                <>
                  <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
                    <h2 style={{fontSize: '1rem', color: 'var(--text-muted)'}}>Library</h2>
                    <button className="sidebar-toggle-btn" onClick={() => setLeftCollapsed(true)} title="Collapse sidebar">◀</button>
                  </div>
                  <BookLoader
                    status={bookStatus}
                    setStatus={setBookStatus}
                    progress={progress}
                    setProgress={setProgress}
                    onLoaded={handleBookLoaded}
                  />
              
              {bookStatus === 'done' && (
                <div className={`glass-card ${!selectedCharacter ? 'pulse-border' : ''}`} style={{padding: '20px'}}>
                  <div className="section-header" style={{marginBottom: '16px'}}>
                    <h2 style={{fontSize: '1rem'}}>Active Character</h2>
                  </div>
                  <div style={{display: 'flex', gap: '8px'}}>
                    <input
                      list="character-list"
                      className="input"
                      style={{flex: 1}}
                      placeholder="Type or select..."
                      value={customCharInput}
                      onChange={(e) => setCustomCharInput(e.target.value)}
                      onKeyDown={(e) => {
                        if (e.key === 'Enter' && customCharInput.trim()) {
                          handleCharacterSelect(customCharInput.trim())
                        }
                      }}
                      disabled={charDetailsLoading}
                    />
                    <datalist id="character-list">
                      {characters.map((c) => (
                        <option key={c} value={c} />
                      ))}
                    </datalist>
                    <button
                      className="btn btn-primary"
                      style={{padding: '8px 12px'}}
                      onClick={() => handleCharacterSelect(customCharInput.trim())}
                      disabled={charDetailsLoading || !customCharInput.trim()}
                    >
                      Search
                    </button>
                  </div>
                  {charError && (
                    <div className="error-badge" style={{marginTop: '10px', fontSize: '0.9rem', padding: '10px', borderRadius: '8px', background: 'rgba(255, 68, 68, 0.1)', color: 'var(--error)', border: '1px solid var(--error)'}}>
                      ✗ {charError}
                    </div>
                  )}

                  {/* Description Carousel — below the search input, inside the same card */}
                  <DescriptionCarousel
                    bookName={currentBookName}
                    selectedCharacter={selectedCharacter}
                    onSelectCharacter={handleCharacterSelect}
                    refreshToken={carouselRefresh}
                  />
                </div>
              )}
              {carouselRefresh && null /* Trigger re-render if needed */}
                </>
              )}
            </div>

            {/* Main Center: Details, Scenarios, Prompting */}
            <div className="dashboard-main">
              {bookStatus === 'done' && (
                <nav className="tabs-nav animate-in">
                  <button 
                    className={`tab-btn ${activeTab === 'generator' ? 'active' : ''}`}
                    onClick={() => setActiveTab('generator')}
                  >
                    <span className="tab-icon">🎨</span> Character Studio
                  </button>
                  <button 
                    className={`tab-btn ${activeTab === 'agents' ? 'active' : ''}`}
                    onClick={() => setActiveTab('agents')}
                  >
                    <span className="tab-icon">🤖</span> AI Agents
                  </button>
                  <button 
                    className={`tab-btn ${activeTab === 'gallery' ? 'active' : ''}`}
                    onClick={() => setActiveTab('gallery')}
                  >
                    <span className="tab-icon">🖼️</span> Character Gallery
                  </button>
                  <button 
                    className={`tab-btn ${activeTab === 'locations' ? 'active' : ''}`}
                    onClick={() => setActiveTab('locations')}
                  >
                    <span className="tab-icon">📍</span> Locations
                  </button>
                </nav>
              )}

              {activeTab === 'generator' && (
                <>
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
                          setPrompt={setPrompt}
                          savedPrompts={savedPrompts}
                          loading={promptLoading}
                          onGenerate={handleGeneratePrompt}
                          onSave={handleSavePrompt}
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
                    <div className="glass-card animate-in" style={{textAlign: 'center', padding: '100px 40px', color: 'var(--text-faint)'}}>
                      <div style={{fontSize: '4rem', marginBottom: '20px', animation: 'pulseObj 2s infinite'}}>🎭</div>
                      <h2 style={{color: 'var(--text)', marginBottom: '12px'}}>Ready to Cast</h2>
                      <p style={{marginBottom: '24px'}}>Select a character from the sidebar to begin generating their description and media prompts.</p>
                      <div style={{display: 'inline-block', background: 'rgba(168, 85, 247, 0.1)', padding: '16px 24px', borderRadius: '8px', border: '1px solid rgba(168, 85, 247, 0.3)'}}>
                        <p style={{margin: 0, fontSize: '0.85rem', color: 'var(--purple)'}}>
                          💡 <strong>Tip:</strong> Head to the <strong>AI Agents</strong> tab to auto-analyze multiple characters or find shared group scenes.
                        </p>
                      </div>
                    </div>
                  )}
                </>
              )}

              {activeTab === 'agents' && bookStatus === 'done' && (
                <div className="agents-grid animate-in">
                  <GroupSceneFinder 
                    characters={characters}
                    llmProvider={llmProvider}
                    onSelectScenario={setSelectedScenario}
                    onSendPrompt={handleSendToGen}
                    onAgentDone={() => setCarouselRefresh(t => t + 1)}
                    initiallyOpen={true}
                  />
                  
                  <BatchImageGenerator 
                    bookName={currentBookName}
                    onAgentDone={() => setCarouselRefresh(t => t + 1)}
                    initiallyOpen={true}
                  />
                </div>
              )}

              {activeTab === 'gallery' && bookStatus === 'done' && (
                <div className="gallery-grid animate-in" style={{marginTop: '20px'}}>
                  <CharacterGallery 
                    bookName={currentBookName}
                    onEditCharacter={(name) => {
                      setActiveTab('generator');
                      handleCharacterSelect(name);
                    }}
                    onSendPrompt={handleSendToGen}
                    llmProvider={llmProvider}
                    onDeleted={() => setCarouselRefresh(t => t + 1)}
                  />
                </div>
              )}

              {activeTab === 'locations' && bookStatus === 'done' && (
                <div className="animate-in" style={{ marginTop: '0' }}>
                  <LocationsPanel
                    bookName={currentBookName}
                    llmProvider={llmProvider}
                  />
                </div>
              )}
            </div>

            {/* Sidebar Right: Prompt History & ComfyUI */}
            <div className={`dashboard-right ${rightCollapsed ? 'collapsed' : ''}`}>
              {rightCollapsed ? (
                <div className="glass-card collapsed-content" style={{height: '100%', cursor: 'pointer'}} onClick={() => setRightCollapsed(false)}>
                  <button className="sidebar-toggle-btn">◀</button>
                  <div className="collapsed-text">GENERATOR</div>
                </div>
              ) : (
                <>
                  <div style={{display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
                    <button className="sidebar-toggle-btn" onClick={() => setRightCollapsed(true)} title="Collapse sidebar">▶</button>
                    <h2 style={{fontSize: '1rem', color: 'var(--text-muted)'}}>Output</h2>
                  </div>
                  {/* ComfyUI Section — Always Visible */}
                  <ComfyPanel
                    ref={comfyRef}
                    prompt={prompt}
                    characterName={selectedCharacter}
                    bookName={currentBookName}
                    onImageSaved={() => setCarouselRefresh(t => t + 1)}
                  />

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
                        <div style={{color: 'var(--text-muted)', fontSize: '0.7rem', display: 'flex', justifyContent: 'space-between', alignItems: 'center'}}>
                          <span>{item.genre} | {item.scenario}</span>
                          {renderPromptBadge(item.prompt)}
                        </div>
                        <div style={{marginTop: '8px', display: 'flex', gap: '8px', opacity: 0.8}}>
                          <button 
                            className="btn btn-secondary" 
                            style={{fontSize: '0.65rem', padding: '4px 8px', flex: 1}}
                            onClick={(e) => { e.stopPropagation(); handleSendToGen(item.prompt, true); }}
                          >
                            🚀 Send to Image Gen
                          </button>
                          <button 
                            className="btn btn-secondary" 
                            style={{fontSize: '0.65rem', padding: '4px 8px', flex: 1}}
                            onClick={(e) => { e.stopPropagation(); handleSendToGen(item.prompt, false); }}
                          >
                            🎬 Send to Video Gen
                          </button>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}
                </>
              )}
            </div>
          </>
        )}
      </main>
    </div>
  )
}
