import React from 'react';

export const renderPromptBadge = (promptText) => {
  if (!promptText) return null;
  const isVideo = /(camera|pan|tracking shot|zoom|motion|slow motion)/i.test(promptText);
  return isVideo ? (
    <span style={{ fontSize: '0.65rem', padding: '2px 6px', background: 'rgba(6, 182, 212, 0.2)', color: '#22d3ee', border: '1px solid #22d3ee', borderRadius: '12px', fontWeight: 'bold' }}>🎥 VIDEO</span>
  ) : (
    <span style={{ fontSize: '0.65rem', padding: '2px 6px', background: 'rgba(168, 85, 247, 0.2)', color: '#c084fc', border: '1px solid #c084fc', borderRadius: '12px', fontWeight: 'bold' }}>🖼️ IMAGE</span>
  );
};
