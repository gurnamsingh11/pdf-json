# from pdf_markdown import pdf_to_markdown
from pdf_markdown import pdf_markdown
from markdown_json import generate
import json
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from io import BytesIO
import tempfile
import re



app = FastAPI()



@app.post("/convert-pdf/")
async def convert_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(await file.read())
            tmp_path = tmp.name
        
        markdown_content = pdf_markdown(tmp_path)
        json_content = generate(markdown_content)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Conversion error: {str(e)}")
    
    if not markdown_content:
        raise HTTPException(status_code=204, detail="No content extracted.")

    return json_content