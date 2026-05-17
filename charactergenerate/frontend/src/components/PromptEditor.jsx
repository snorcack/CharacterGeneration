import React, { useRef, useState, useEffect } from 'react';

// Regex patterns for highlighting
const PATTERNS = [
  // Camera movements
  { regex: /\b(pan|zoom|tilt|dolly|tracking|crane|static|slow motion|fast motion)\b/gi, color: 'var(--gold)' },
  // Lighting
  { regex: /\b(cinematic lighting|volumetric|neon|backlit|ambient|harsh|soft|dark|bright|shadows?)\b/gi, color: '#3b82f6' },
  // Key physical/character descriptors
  { regex: /\[([^\]]+)\]/g, color: 'var(--purple)' }, // Highlights bracketed tags like [ 🎥 VIDEO ]
  // Quality tags
  { regex: /\b(masterpiece|best quality|8k|4k|high resolution)\b/gi, color: '#10b981' },
];

function highlightText(text) {
  if (!text) return '';
  
  // We need to carefully wrap words without messing up HTML tags we inject.
  // The simplest approach is to escape HTML first, then apply regex replaces.
  let escaped = text
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

  PATTERNS.forEach(({ regex, color }) => {
    escaped = escaped.replace(regex, `<span style="color: ${color}; font-weight: 600;">$&</span>`);
  });

  // Preserve newlines
  return escaped.replace(/\n/g, '<br/>');
}

export default function PromptEditor({ value, onChange, placeholder, style, readOnly = false }) {
  const [html, setHtml] = useState('');
  const textareaRef = useRef(null);
  const backdropRef = useRef(null);

  useEffect(() => {
    setHtml(highlightText(value));
  }, [value]);

  const handleScroll = () => {
    if (backdropRef.current && textareaRef.current) {
      backdropRef.current.scrollTop = textareaRef.current.scrollTop;
      backdropRef.current.scrollLeft = textareaRef.current.scrollLeft;
    }
  };

  const baseStyle = {
    fontFamily: 'inherit',
    fontSize: '0.85rem',
    lineHeight: '1.5',
    padding: '12px',
    margin: 0,
    border: 'none',
    width: '100%',
    height: '100%',
    whiteSpace: 'pre-wrap',
    wordWrap: 'break-word',
    boxSizing: 'border-box',
    overflowY: 'auto'
  };

  return (
    <div style={{ position: 'relative', width: '100%', height: style?.height || '150px', ...style }}>
      {/* Highlight Backdrop */}
      <div 
        ref={backdropRef}
        style={{
          ...baseStyle,
          position: 'absolute',
          top: 0,
          left: 0,
          background: 'rgba(0,0,0,0.2)', // Same as textarea background
          color: 'var(--text)',
          pointerEvents: 'none',
          borderColor: 'transparent',
          zIndex: 1,
        }}
        dangerouslySetInnerHTML={{ __html: html + (value && value.endsWith('\n') ? '<br/>' : '') }}
      />
      {/* Interactive Textarea */}
      <textarea
        ref={textareaRef}
        value={value}
        onChange={(e) => onChange(e.target.value)}
        onScroll={handleScroll}
        placeholder={placeholder}
        readOnly={readOnly}
        spellCheck="false"
        style={{
          ...baseStyle,
          position: 'absolute',
          top: 0,
          left: 0,
          background: 'transparent',
          color: 'transparent',
          caretColor: 'var(--text)',
          zIndex: 2,
          outline: 'none',
          resize: 'none',
          border: '1px solid var(--border)',
          borderRadius: '8px',
        }}
      />
    </div>
  );
}
