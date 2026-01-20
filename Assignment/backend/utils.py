# utils.py
from docx import Document
from fpdf import FPDF

def generate_docx(content, filename="resume.docx"):
    """Generate a Word resume"""
    doc = Document()
    doc.add_paragraph(content)
    doc.save(filename)
    return filename

def generate_pdf(content, filename="resume.pdf"):
    """Generate a PDF resume"""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, content)
    pdf.output(filename)
    return filename
