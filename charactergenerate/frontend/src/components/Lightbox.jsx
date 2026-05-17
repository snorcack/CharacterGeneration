import React, { useEffect } from 'react';

export default function Lightbox({ src, alt, onClose }) {
  useEffect(() => {
    const handleKeyDown = (e) => {
      if (e.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [onClose]);

  if (!src) return null;

  return (
    <div 
      style={{
        position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
        backgroundColor: 'rgba(0, 0, 0, 0.9)',
        backdropFilter: 'blur(8px)',
        zIndex: 10000,
        display: 'flex', alignItems: 'center', justifyContent: 'center',
        cursor: 'zoom-out',
        animation: 'fadeIn 0.2s ease-out'
      }}
      onClick={onClose}
    >
      <div 
        className="animate-in"
        style={{ position: 'relative', maxWidth: '90vw', maxHeight: '90vh' }}
        onClick={(e) => e.stopPropagation()} // Prevent click from closing when clicking image
      >
        <button 
          onClick={onClose}
          style={{
            position: 'absolute', top: '-40px', right: 0,
            background: 'none', border: 'none', color: '#fff',
            fontSize: '2rem', cursor: 'pointer', padding: '8px'
          }}
        >
          &times;
        </button>
        <img 
          src={src} 
          alt={alt || "Fullscreen view"} 
          style={{ 
            maxWidth: '100%', maxHeight: '90vh', 
            objectFit: 'contain', borderRadius: '8px', 
            boxShadow: '0 10px 40px rgba(0,0,0,0.8)',
            border: '1px solid rgba(255,255,255,0.1)'
          }} 
        />
      </div>
    </div>
  );
}
