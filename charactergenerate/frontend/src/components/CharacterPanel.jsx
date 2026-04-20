import { Loader } from './Loader'

const INDUSTRIES = [
  { label: 'Hollywood', value: 'hollywood' },
  { label: 'Bollywood', value: 'bollywood' },
  { label: 'Korean', value: 'korean' },
  { label: 'European', value: 'european' },
]

/**
 * CharacterPanel — Section 02
 * Character dropdown → editable description textarea → industry + cast → actor override.
 */
export default function CharacterPanel({
  characters,
  selectedCharacter,
  onSelectCharacter,
  charDetailsLoading,
  description,
  setDescription,
  industry,
  setIndustry,
  genre,
  setGenre,
  decade,
  setDecade,
  actorName,
  setActorName,
  actorLoading,
  onCastActor,
  minimal = false,
}) {
  const hasDetails = !charDetailsLoading && selectedCharacter && description

  return (
    <section className="glass-card animate-in">
      {!minimal && (
        <div className="section-header">
          <span className="section-number">02</span>
          <div>
            <h2>Character</h2>
            <p className="section-subtitle">
              Select a character, refine their description, then cast an actor
            </p>
          </div>
        </div>
      )}

      {!minimal && (
        <div className="form-group">
          <label htmlFor="character-select">Select Character</label>
          <div className="select-wrapper">
            <select
              id="character-select"
              className="select"
              value={selectedCharacter}
              onChange={(e) => onSelectCharacter(e.target.value)}
              disabled={charDetailsLoading}
            >
              <option value="">— Choose a character —</option>
              {characters.map((c) => (
                <option key={c} value={c}>
                  {c}
                </option>
              ))}
            </select>
          </div>
        </div>
      )}

      {/* Loading state */}
      {charDetailsLoading && (
        <div className="loading-row">
          <Loader />
          <span>Analyzing character and retrieving book scenes… this may take a moment.</span>
        </div>
      )}

      {/* Details — only shown once loaded */}
      {hasDetails && (
        <>
          {/* Editable description */}
          <div className="form-group">
            <label htmlFor="char-description">
              Character Description
              <span className="label-hint">Edit to correct or add missing details</span>
            </label>
            <textarea
              id="char-description"
              className="textarea"
              rows={7}
              value={description}
              onChange={(e) => setDescription(e.target.value)}
              placeholder="Character description will appear here…"
            />
          </div>

          <div className="form-row">
            <div className="form-group">
              <label htmlFor="genre-input">Adaptation Genre</label>
              <input 
                id="genre-input"
                type="text" 
                className="input" 
                value={genre} 
                onChange={e => setGenre(e.target.value)}
                placeholder="e.g. Cyberpunk, Victorian..."
              />
            </div>
            <div className="form-group">
              <label htmlFor="decade-select">Production Decade</label>
              <div className="select-wrapper">
                <select 
                  id="decade-select"
                  className="select" 
                  value={decade} 
                  onChange={e => setDecade(e.target.value)}
                >
                  <option value="modern">Modern (2026)</option>
                  <option value="2010">2010s</option>
                  <option value="2000">2000s</option>
                  <option value="1990">1990s</option>
                  <option value="1980">1980s</option>
                  <option value="1970">1970s</option>
                  <option value="1960">1960s</option>
                  <option value="1950">1950s</option>
                  <option value="1940">1940s</option>
                  <option value="1930">1930s</option>
                </select>
              </div>
            </div>
          </div>

          {/* Industry + Cast row */}
          <div className="cast-row">
            <div className="form-group flex-1">
              <label htmlFor="industry-select">Industry</label>
              <div className="select-wrapper">
                <select
                  id="industry-select"
                  className="select"
                  value={industry}
                  onChange={(e) => setIndustry(e.target.value)}
                >
                  {INDUSTRIES.map((ind) => (
                    <option key={ind.value} value={ind.value}>
                      {ind.label}
                    </option>
                  ))}
                </select>
              </div>
            </div>

            <button
              id="cast-actor-btn"
              className="btn btn-secondary cast-btn"
              onClick={onCastActor}
              disabled={actorLoading || !description.trim()}
            >
              {actorLoading ? (
                <><Loader small /> Casting…</>
              ) : (
                '🎬 Cast Actor'
              )}
            </button>
          </div>

          {/* Actor override field */}
          {actorName && (
            <div className="form-group actor-override">
              <label htmlFor="actor-name">
                Cast Actor
                <span className="label-hint">Override by typing a different name</span>
              </label>
              <input
                id="actor-name"
                type="text"
                className="input actor-input"
                value={actorName}
                onChange={(e) => setActorName(e.target.value)}
                placeholder="Actor name…"
              />
            </div>
          )}
        </>
      )}
    </section>
  )
}
