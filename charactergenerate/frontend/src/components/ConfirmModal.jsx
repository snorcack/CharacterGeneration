import React from 'react';

export default function ConfirmModal({ isOpen, title, message, onConfirm, onCancel, confirmText = "Confirm", cancelText = "Cancel", destructive = false }) {
  if (!isOpen) return null;

  return (
    <div style={{
      position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.75)',
      backdropFilter: 'blur(4px)',
      display: 'flex', alignItems: 'center', justifyContent: 'center',
      zIndex: 9999,
      animation: 'fadeIn 0.2s ease-out'
    }}>
      <div className="glass-card animate-in" style={{
        padding: '24px', maxWidth: '400px', width: '90%',
        backgroundColor: '#1a1a1a', border: '1px solid var(--border)',
        borderRadius: '12px', boxShadow: '0 10px 25px rgba(0,0,0,0.5)'
      }}>
        <h3 style={{ margin: '0 0 12px 0', fontSize: '1.2rem', color: destructive ? '#ff4444' : 'var(--text)' }}>
          {title}
        </h3>
        <p style={{ margin: '0 0 24px 0', fontSize: '0.9rem', color: 'var(--text-muted)', lineHeight: '1.5' }}>
          {message}
        </p>
        <div style={{ display: 'flex', gap: '12px', justifyContent: 'flex-end' }}>
          <button className="btn btn-secondary" onClick={onCancel}>
            {cancelText}
          </button>
          <button 
            className="btn btn-primary" 
            onClick={onConfirm}
            style={{ 
              backgroundColor: destructive ? '#ff4444' : 'var(--purple)',
              borderColor: destructive ? '#cc0000' : 'var(--purple)'
            }}
          >
            {confirmText}
          </button>
        </div>
      </div>
    </div>
  );
}
