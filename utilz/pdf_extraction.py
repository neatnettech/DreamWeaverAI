import os
from PyPDF2 import PdfReader

PDF_DIRECTORY = "RAG"

def list_available_pdfs():
    return [f for f in os.listdir(PDF_DIRECTORY) if f.endswith('.pdf')]

def extract_text_from_pdf(filename):
    file_path = os.path.join(PDF_DIRECTORY, filename)
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text