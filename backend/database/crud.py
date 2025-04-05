from uuid import UUID
from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.claims import Claim


def create_claim(db: Session, claim_data):
    new_claim = Claim(**claim_data.dict())
    db.add(new_claim)
    db.commit()
    db.refresh(new_claim)
    return new_claim

def get_claim(db: Session, claim_id: UUID):
    return db.query(Claim).filter(Claim.id == claim_id).first()

def get_all_claims(db: Session):
    return db.query(Claim).all()
   
def update_claim_status(db: Session, claim_id: UUID, claim_data):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if not claim:
        raise HTTPException(status_code=404, detail="Claim not found")
    
    if claim_data.claim_amount is not None:
        claim.claim_amount = claim_data.claim_amount

    if claim_data.description is not None:
        claim.description = claim_data.description

    if claim_data.claim_status is not None:
        claim.claim_status = claim_data.claim_status

    if claim_data.fraud_flag is not None:
        claim.fraud_flag = claim_data.fraud_flag
    

    db.commit()
    db.refresh(claim)
    return claim

def delete_claim(db: Session, claim_id: UUID):
    claim = db.query(Claim).filter(Claim.id == claim_id).first()
    if claim:
        db.delete(claim)
        db.commit()
    return claim