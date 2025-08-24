"""
Data Loader Module
------------------
Handles ingestion of multimodal data sources (text, PDF, images).
"""

import fitz  # PyMuPDF for PDFs
from PIL import Image
import pytesseract

def load_text(file_path: str) -> str:
    """Load plain text file."""
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf(file_path: str) -> str:
    """Extract text from a PDF file."""
    doc = fitz.open(file_path)
    text = " ".join([page.get_text() for page in doc])
    return text.strip()

def load_image(file_path: str) -> str:
    """Extract text from image using OCR."""
    img = Image.open(file_path)
    return pytesseract.image_to_string(img)
