import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [message, setMessage] = useState('')

  useEffect(() => {
    fetch('/api/hello')
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(err => {
        console.error(err)
        setMessage('Failed to fetch from backend')
      })
  }, [])

  return (
    <div className="app">
      <h1>{message || 'Loading...'}</h1>
    </div>
  )
}

export default App
