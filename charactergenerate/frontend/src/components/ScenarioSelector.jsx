/**
 * ScenarioSelector — Section 03
 * Dropdown populated from RAG-retrieved and LLM-summarised book scenes.
 * Shows a text excerpt of the selected scene below the dropdown.
 */
export default function ScenarioSelector({ scenarios, selectedScenario, onSelectScenario }) {
  const handleChange = (e) => {
    const found = scenarios.find((s) => s.label === e.target.value)
    onSelectScenario(found ?? null)
  }

  return (
    <section className="glass-card animate-in">
      <div className="section-header">
        <span className="section-number">03</span>
        <div>
          <h2>Scene</h2>
          <p className="section-subtitle">
            Choose a real scene from the book to set the stage for the image
          </p>
        </div>
      </div>

      <div className="form-group">
        <label htmlFor="scenario-select">Select Scene / Scenario</label>
        <div className="select-wrapper">
          <select
            id="scenario-select"
            className="select"
            value={selectedScenario?.label ?? ''}
            onChange={handleChange}
          >
            <option value="">— Choose a scene —</option>
            {scenarios.map((s, i) => (
              <option key={i} value={s.label}>
                {s.label}
              </option>
            ))}
          </select>
        </div>
      </div>

      {selectedScenario && (
        <div className="scene-preview">
          <div className="scene-preview-label">Scene excerpt from book</div>
          <p className="scene-text">
            {selectedScenario.context.slice(0, 420)}
            {selectedScenario.context.length > 420 ? '…' : ''}
          </p>
        </div>
      )}
    </section>
  )
}
