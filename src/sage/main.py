import asyncio
import uvicorn
from fastapi import FastAPI, Body
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import os
import signal

from .core.llm_provider import LLMProvider
from .core.git_manager import GitManager

# --- Pydantic Models ---
class AskRequest(BaseModel):
    prompt: str

# --- FastAPI App ---
app = FastAPI()

# --- Core Logic Instances ---
gemini_provider = LLMProvider(provider_cli_command="gemini")
# The repo_path is relative to the execution directory (src), so we go up one level.
git_manager = GitManager(repo_path="..") 

# --- API Endpoints ---
@app.post("/ask")
async def ask(request: AskRequest):
    response = await gemini_provider.ask(request.prompt)
    return {"response": response}

@app.get("/git/status")
async def get_git_status():
    status = git_manager.get_status()
    confirmed_status = f"Successfully retrieved Git status:\n---\n{status}"
    return {"status": confirmed_status}

@app.get("/shutdown")
async def shutdown():
    # This will send a SIGINT (Ctrl+C) to the current process, which Uvicorn will catch to shut down gracefully.
    os.kill(os.getpid(), signal.SIGINT)
    return {"message": "Server is shutting down..."}

# --- Static Files ---
# Mount the UI directory to serve static files (HTML, CSS, JS)
# The path is relative to this file's location (src/sage/main.py)
app.mount("/", StaticFiles(directory="../../ui", html=True), name="ui")

# --- Main Entry Point ---
def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()