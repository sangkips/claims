import os
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import requests
import tempfile
from sqlalchemy.orm import Session

from services.nlp_service import classify_document
from models.claims import OCRResult

PINATA_API_KEY = os.getenv("PINATA_API_KEY")
PINATA_SECRET_API_KEY = os.getenv("PINATA_SECRET_API_KEY")
PINATA_GATEWAY = os.getenv("PINATA_GATEWAY", "https://gateway.pinata.cloud/ipfs")

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
   
def upload_to_pinata(filepath: str) -> str:
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {
        "pinata_api_key": PINATA_API_KEY,
        "pinata_secret_api_key": PINATA_SECRET_API_KEY
    }
 
    with open(filepath, "rb") as file:
        files = {"file": (os.path.basename(filepath), file)}
        response = requests.post(url, files=files, headers=headers)

        if response.status_code != 200:
            raise Exception("Failed to upload to Pinata")
        ipfs_hash = response.json()["IpfsHash"]
        return f"{PINATA_GATEWAY}/{ipfs_hash}"

def extract_text_from_file(file_path: str) -> str:
    text = ""
    if file_path.lower().endswith(".pdf"):
        try:
            # Use pdf2image to convert PDF to images
            images = convert_from_path(file_path)
            for img in images:
                text += pytesseract.image_to_string(img)
        except Exception as e:
            raise Exception(f"Failed to process PDF: {str(e)}")
    else:
        try:
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
        except Exception as e:
            raise Exception(f"Failed to process image: {str(e)}")
    
    return text

async def upload_and_process_document(claim_id: str, file, db: Session):
    file_extension = os.path.splitext(file.filename)[1]
    
    with tempfile.NamedTemporaryFile(suffix=file_extension, delete=False) as tmp:
        content = await file.read()
        tmp.write(content)
        tmp_path = tmp.name

    # Upload to Pinata
    document_url = upload_to_pinata(tmp_path)

    # Extract text
    extracted_text = extract_text_from_file(tmp_path)

    classification = classify_document(extracted_text)

    # Save to DB
    result = OCRResult(
        claim_id=claim_id,
        document_path=document_url,
        extracted_text=extracted_text,
        classification=classification
    )
    db.add(result)
    db.commit()
    db.refresh(result)

    return {"message": "Document processed", "data": {
        "document_url": document_url,
        "extracted_text": extracted_text[:100] + "..." if len(extracted_text) > 100 else extracted_text
    }}