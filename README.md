# React + FastAPI App

This repository provides a minimal example of a React front‑end created with Vite and a Python back‑end powered by FastAPI.

## Requirements
- Node.js
- Python 3.10+

## Install dependencies
```bash
npm install
python -m pip install -r backend/requirements.txt
```

## Development
Start the back end:
```bash
uvicorn backend.main:app --reload
```

In another terminal start the front end:
```bash
npm run dev
```

The React app will be available at <http://localhost:5173> and will fetch data from the FastAPI server running on <http://localhost:8000>.

