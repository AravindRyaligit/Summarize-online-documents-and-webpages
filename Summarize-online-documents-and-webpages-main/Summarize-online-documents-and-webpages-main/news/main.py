from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from services.summarizer import summarize_text
from services.llm_groq import summarize_url, summarize_urls_parallel
from pydantic import BaseModel
from typing import List, Union
import uvicorn
import logging

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SummarizeRequest(BaseModel):
    type: str
    content: Union[str, List[str]]

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/summarize")
async def api_summarize(request: SummarizeRequest):
    """API endpoint for summarization from frontend"""
    try:
        if request.type == "text":
            if not isinstance(request.content, str) or not request.content.strip():
                raise HTTPException(status_code=400, detail="Text content cannot be empty")
            summary = summarize_text(request.content)
        elif request.type == "urls":
            if not isinstance(request.content, list) or len(request.content) == 0:
                raise HTTPException(status_code=400, detail="At least one URL is required")
            summaries = summarize_urls_parallel(request.content)
            if len(summaries) == 1:
                summary = summaries[0]
            else:
                summary = "\n\n---\n\n".join(summaries)
        else:
            raise HTTPException(status_code=400, detail="Invalid type. Must be 'text' or 'urls'")
        
        return JSONResponse({"summary": summary})
    except Exception as e:
        logger.error(f"Summarization error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize", response_class=HTMLResponse)
async def summarize(request: Request, content: str = Form(...)):
    if not content.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty.")
    
    result = summarize_text(content)
    if not result:
        raise HTTPException(status_code=500, detail="Summarization failed.")
    
    return templates.TemplateResponse(
        "index.html", {"request": request, "result": result}
    )

@app.post("/compare")
async def compare(request: Request, text1: str = Form(...), text2: str = Form(...)):
    compare_result = f"Comparison between: '{text1[:50]}...' and '{text2[:50]}...'"
    return templates.TemplateResponse(
        "index.html", {"request": request, "compare_result": compare_result}
    )

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)