import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'

createRoot(document.getElementById('root')!).render(
  /*  <StrictMode> dev model tag, production will be igored,
      Intentionally renders components twice to help detect side effect issues (e.g. code inside useEffect that should not run more than once)
      Detects deprecated APIs — if you use any syntax that React has phased out, it will throw a warning in the console */
  <StrictMode>
    <App />
  </StrictMode>,
)
