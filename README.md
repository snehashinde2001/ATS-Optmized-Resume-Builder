# ATS-Optimized Resume Builder

## 📌 Project Overview
This project is an **AI-powered Resume Builder & ATS Optimization Agent**.  
It helps candidates create ATS-friendly resumes with professional formatting and enhanced readability.  
Users can upload an existing resume or manually enter details, and the system automatically optimizes the content using AI.

---

## 🚀 Features
- Upload existing resume (PDF/Word) or enter details manually  
- Resume parsing (extracts text and structures data)  
- ATS scoring via API integration  
- AI enhancement using OpenAI + Gemini APIs  
- Pre-integrated LaTeX templates for professional formatting  
- Generates resumes in **Word (.docx)** and **PDF** formats  
- Displays ATS score before and after enhancement  
- Bonus features: Live preview, comparison mode, score tracker, feedback chat  

---

## 🛠️ Tech Stack
- **Backend:** FastAPI (Python)  
- **Frontend:** Next.js (React)  
- **Resume Parsing:** PyPDF2, python-docx  
- **AI Enhancement:** OpenAI API, Gemini API  
- **Formatting:** LaTeX templates (AutoCV, AwesomeCV)  
- **Export:** python-docx, fpdf  

---

## ⚙️ Installation & Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
