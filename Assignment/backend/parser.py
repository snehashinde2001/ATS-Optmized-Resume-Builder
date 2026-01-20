# parser.py
import PyPDF2
import docx

def parse_pdf(file_path):
    """Extract text from a PDF resume"""
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text

def parse_docx(file_path):
    """Extract text from a Word resume"""
    doc = docx.Document(file_path)
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def parse_resume(file_path):
    """Detect file type and parse accordingly"""
    if file_path.endswith(".pdf"):
        return parse_pdf(file_path)
    elif file_path.endswith(".docx"):
        return parse_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX.")
