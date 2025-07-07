### main.py

from fastapi import FastAPI, Request, Form, Cookie
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import uuid

from ia_engine import GiftAssistantAgent

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dictionnaire des agents actifs (clé = session ID)
agents: dict[str, GiftAssistantAgent] = {}

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask_question(
    request: Request,
    question: str = Form(...),
    session_id: str = Cookie(default=None)
):
    if not session_id or session_id not in agents:
        session_id = str(uuid.uuid4())
        agents[session_id] = GiftAssistantAgent()

    agent = agents[session_id]
    response_text = agent.generate(question)

    return JSONResponse(
        {"response": response_text, "history": agent.history},
        headers={"set-cookie": f"session_id={session_id}; Path=/;"}
    )
