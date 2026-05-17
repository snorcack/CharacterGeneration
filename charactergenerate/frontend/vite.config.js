import path from 'path'
import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

// Repo root is two levels above the frontend directory
const REPO_ROOT = path.resolve(__dirname, '../../')

export default defineConfig(({ mode }) => {
  // Load all env vars (no VITE_ prefix filter) from the repo root .env
  const env = loadEnv(mode, REPO_ROOT, '')

  const port        = parseInt(env.VITE_PORT        || '5173', 10)
  const backendUrl  = env.VITE_BACKEND_URL           || 'http://localhost:8000'

  return {
    plugins: [react()],
    server: {
      port,
      proxy: {
        '/api': {
          target: backendUrl,
          changeOrigin: true,
        },
      },
    },
  }
})
