# main.py
from fastapi import FastAPI, UploadFile, Form
from pydantic import BaseModel
import tempfile

from parser import parse_resume
from ats_api import get_ats_score
from ai_enhancer import enhance_resume
from utils import generate_docx, generate_pdf

app = FastAPI(title="AI-Powered Resume Builder")

class ResumeData(BaseModel):
    personal_info: dict
    education: list
    skills: list
    experience: list
    projects: list

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile):
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(await file.read())
    temp_file.close()
    parsed_text = parse_resume(temp_file.name)
    return {"parsed_text": parsed_text}

@app.post("/manual_entry/")
async def manual_entry(data: ResumeData):
    return {"message": "Manual data received", "data": data.dict()}

@app.post("/ats_score/")
async def ats_score(data: ResumeData):
    resume_text = " ".join(data.skills + [exp["description"] for exp in data.experience])
    score = get_ats_score(resume_text)
    return {"ats_score": score}

@app.post("/enhance_resume/")
async def enhance(data: ResumeData, job_description: str = Form("")):
    resume_text = " ".join(data.skills + [exp["description"] for exp in data.experience])
    enhanced = enhance_resume(resume_text, job_description)
    return {"enhanced_resume": enhanced}

@app.post("/generate_resume/")
async def generate(enhanced_resume: str):
    docx_file = generate_docx(enhanced_resume)
    pdf_file = generate_pdf(enhanced_resume)
    return {"docx_file": docx_file, "pdf_file": pdf_file}
