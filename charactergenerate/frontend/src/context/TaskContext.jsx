import React, { createContext, useContext, useState, useCallback } from 'react';

const TaskContext = createContext(null);

export const useTasks = () => {
  const context = useContext(TaskContext);
  if (!context) throw new Error('useTasks must be used within a TaskProvider');
  return context;
};

export const TaskProvider = ({ children }) => {
  const [tasks, setTasks] = useState({});

  const setTaskProgress = useCallback((taskId, data) => {
    setTasks(prev => {
      // If done or error and progress is complete, we might want to keep it around for a few seconds then remove it.
      // For now, we just update it.
      return { ...prev, [taskId]: { ...prev[taskId], ...data, id: taskId, updatedAt: Date.now() } };
    });
  }, []);

  const clearTask = useCallback((taskId) => {
    setTasks(prev => {
      const newTasks = { ...prev };
      delete newTasks[taskId];
      return newTasks;
    });
  }, []);

  return (
    <TaskContext.Provider value={{ tasks, setTaskProgress, clearTask }}>
      {children}
      <TaskWidget tasks={tasks} clearTask={clearTask} />
    </TaskContext.Provider>
  );
};

const TaskWidget = ({ tasks, clearTask }) => {
  const activeTasks = Object.values(tasks).filter(t => t.status && t.status !== 'idle');
  
  if (activeTasks.length === 0) return null;

  return (
    <div style={{
      position: 'fixed',
      bottom: '24px',
      left: '24px',
      width: '320px',
      display: 'flex',
      flexDirection: 'column',
      gap: '12px',
      zIndex: 9999,
      pointerEvents: 'none' // container is passthrough
    }}>
      {activeTasks.map(task => (
        <div key={task.id} className="glass-card animate-in" style={{ padding: '16px', margin: 0, pointerEvents: 'auto', boxShadow: '0 8px 30px rgba(0,0,0,0.6)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '8px' }}>
            <span style={{ fontSize: '0.85rem', fontWeight: '600', color: task.status === 'error' ? 'var(--error)' : 'var(--text)' }}>
              {task.title}
            </span>
            {(task.status === 'done' || task.status === 'error') && (
              <button 
                onClick={() => clearTask(task.id)}
                style={{ background: 'none', border: 'none', color: 'var(--text-faint)', cursor: 'pointer', fontSize: '1rem' }}
              >
                &times;
              </button>
            )}
          </div>
          
          {task.status === 'running' || task.status === 'queued' ? (
            <div className="progress-track" style={{ height: '4px', marginBottom: '8px', background: 'rgba(255,255,255,0.1)' }}>
              <div 
                className="progress-fill" 
                style={{ 
                  width: task.total > 0 ? `${(task.progress / task.total) * 100}%` : (task.status === 'queued' ? '100%' : '50%'),
                  transition: 'width 0.3s ease',
                  background: task.status === 'queued' ? 'var(--gold)' : 'var(--purple)',
                  animation: task.total > 0 ? 'none' : 'pulse 1.5s infinite'
                }} 
              />
            </div>
          ) : null}

          <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', display: 'flex', justifyContent: 'space-between' }}>
            <span style={{ whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis', maxWidth: '80%' }}>
              {task.message}
            </span>
            {task.total > 0 && <span>{task.progress} / {task.total}</span>}
          </div>
        </div>
      ))}
    </div>
  );
};
