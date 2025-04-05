from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from schemas.claims import ClaimCreate, ClaimUpdate, claimResponse
from database.crud import create_claim, get_all_claims, get_claim, update_claim_status
from database.session import get_db


router = APIRouter()


@router.post("/claims/", response_model=claimResponse)
def submit_claim(claim: ClaimCreate, db: Session = Depends(get_db)):
    return create_claim(db, claim)

@router.get("/claims/")
def get_claims(db: Session = Depends(get_db)):
    claims = get_all_claims(db)
    return claims

@router.get("/claims/{claim_id}")
def get_claims_details(claim_id: str, db: Session = Depends(get_db)):
    claim = get_claim(db, claim_id)
    if not claim:
        return HTTPException(status_code=404, detail="Claim not found")
    return claim

@router.patch("/claims/{claim_id}", response_model=claimResponse)
def update_claim(claim_id: str, update_data: ClaimUpdate, db: Session = Depends(get_db)):
    return update_claim_status(db, claim_id, update_data)

@router.delete("claims/{claim_id}")
def delete_claim(claim_id: str, db: Session = Depends(get_db)):
    claim = get_claim(db, claim_id)
    if not claim:
        return HTTPException(status_code=404, detail="Claim not found")
    db.delete(claim)
    db.commit()
    return {"detail": "Claim deleted successfully"}