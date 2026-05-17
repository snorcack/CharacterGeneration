import { useEffect, useRef, useState } from 'react'

/**
 * DescriptionCarousel
 * Horizontal scrollable strip of character cards below the character search.
 * Each card represents a character whose description has been generated and cached.
 *
 * Props:
 *   bookName         — current book (used to fetch cached data)
 *   selectedCharacter — highlights the active card
 *   onSelectCharacter — callback(charName, cachedEntry) when a card is clicked
 *   refreshToken      — increment to trigger a re-fetch (e.g. after new description is generated)
 */
export default function DescriptionCarousel({
  bookName,
  selectedCharacter,
  onSelectCharacter,
  refreshToken = 0,
}) {
  const [entries, setEntries] = useState({}) // { charName: { description, scenarios, image_prompt_id } }
  const scrollRef = useRef(null)
  const isDragging = useRef(false)
  const startX = useRef(0)
  const scrollLeft = useRef(0)

  // ── Fetch cached descriptions whenever the book changes or refresh token bumps
  useEffect(() => {
    if (!bookName) { setEntries({}); return }
    fetch(`/api/character-descriptions/${encodeURIComponent(bookName)}`)
      .then(r => r.json())
      .then(data => setEntries(data.descriptions || {}))
      .catch(() => setEntries({}))
  }, [bookName, refreshToken])

  const names = Object.keys(entries)
  if (names.length === 0) return null

  // ── Drag-to-scroll helpers
  const onMouseDown = (e) => {
    isDragging.current = true
    startX.current = e.pageX - scrollRef.current.offsetLeft
    scrollLeft.current = scrollRef.current.scrollLeft
    scrollRef.current.style.cursor = 'grabbing'
  }
  const onMouseMove = (e) => {
    if (!isDragging.current) return
    e.preventDefault()
    const x = e.pageX - scrollRef.current.offsetLeft
    scrollRef.current.scrollLeft = scrollLeft.current - (x - startX.current)
  }
  const onMouseUp = () => {
    isDragging.current = false
    if (scrollRef.current) scrollRef.current.style.cursor = 'grab'
  }

  return (
    <div className="desc-carousel-wrapper">
      <div className="desc-carousel-label">
        <span className="section-number" style={{ fontSize: '0.68rem' }}>CACHED</span>
        <span style={{ fontSize: '0.78rem', color: 'var(--text-muted)', fontWeight: 600, letterSpacing: '0.05em', textTransform: 'uppercase' }}>
          Generated Descriptions
        </span>
      </div>

      <div
        className="desc-carousel"
        ref={scrollRef}
        onMouseDown={onMouseDown}
        onMouseMove={onMouseMove}
        onMouseUp={onMouseUp}
        onMouseLeave={onMouseUp}
      >
        {names.map(name => {
          const entry = entries[name]
          const isActive = name === selectedCharacter
          const imageIds = entry.image_prompt_ids || (entry.image_prompt_id ? [entry.image_prompt_id] : [])
          const hasImage = imageIds.length > 0

          return (
            <button
              key={name}
              className={`desc-card ${isActive ? 'desc-card-active' : ''}`}
              onClick={() => onSelectCharacter(name, entry)}
              title={name}
            >
              {hasImage ? (
                <div className="desc-card-img-wrap">
                  <img
                    src={`/api/image/${imageIds[0]}`}
                    alt={name}
                    className="desc-card-img"
                    draggable={false}
                    onError={e => { e.target.style.display = 'none'; e.target.nextSibling.style.display = 'flex' }}
                  />
                  {/* Fallback if image fails to load */}
                  <div className="desc-card-fallback" style={{ display: 'none' }}>
                    <span className="desc-card-initials">{initials(name)}</span>
                  </div>
                </div>
              ) : (
                <div className="desc-card-placeholder">
                  <span className="desc-card-initials">{initials(name)}</span>
                </div>
              )}
              <div className="desc-card-name">{shortName(name)}</div>
              {isActive && <div className="desc-card-active-dot" />}
            </button>
          )
        })}
      </div>
    </div>
  )
}

function initials(name) {
  return name
    .split(/\s+/)
    .filter(Boolean)
    .slice(0, 2)
    .map(w => w[0].toUpperCase())
    .join('')
}

function shortName(name) {
  const parts = name.split(/\s+/)
  if (parts.length <= 2) return name
  // Show first name + last name only for long names
  return `${parts[0]} ${parts[parts.length - 1]}`
}
