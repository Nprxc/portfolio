"""FastAPI backend for gift recommendation assistant."""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from ia_engine import generate_response

# In-memory chat history
chat_history: list[dict[str, str]] = []

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    """Return the chat page."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask_question(question: str = Form(...)):
    """Receive a question and return the AI response with history."""
    # Generate assistant response
    response_text = generate_response(question)

    # Update in-memory history
    chat_history.append({"role": "user", "text": question})
    chat_history.append({"role": "assistant", "text": response_text})

    return JSONResponse({"response": response_text, "history": chat_history})
