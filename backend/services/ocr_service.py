from PIL import Image
import pytesseract
from pdf2image import convert_from_path

def ocr_from_image(image: Image.Image) -> str:
    """
     Extract text from a PIL Image using Tesseract OCR.
    """

    return pytesseract.image_to_string(image)


def ocr_from_pdf(pdf_path: str) -> str:
    """
    Extract text from a PDF file using OCR (converts each page to image).
    """
    pages = convert_from_path(pdf_path)

    text = ""

    for page in pages:
        text += pytesseract.image_to_string(page)
    return text
   