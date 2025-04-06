from io import BytesIO
from fastapi import APIRouter, File, UploadFile, HTTPException
from PIL import Image

from services.ocr_service import ocr_from_image, ocr_from_pdf


router = APIRouter()


@router.post("/ocr/image/")
async def process_image(file: UploadFile = File(...)):
    """
    Process an image file for OCR.
    This endpoint receives an image file, extracts text using OCR,
    """
    try:
        image = Image.open(BytesIO(await file.read()))
        extracted_text = ocr_from_image(image)
        return {"extracted_text": extracted_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/ocr/pdf/")
async def process_pdf(file: UploadFile = File(...)):
    """
    Process a PDF file for OCR.
    This endpoint receives a PDF file, extracts text using OCR,
    """
    try:
        pdf_path = f"temp_{file.filename}"
        with open(pdf_path, "wb") as f:
            f.write(await file.read())
        extracted_text = ocr_from_pdf(pdf_path)
        return {"extracted_text": extracted_text}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))