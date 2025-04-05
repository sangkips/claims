from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID
from enum import Enum

class ClaimStatusEnum(str, Enum):
    """Enumeration for claim status."""
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    UNDER_REVIEW = "Under Review"


class ClaimBase(BaseModel):
    policy_number: str
    claimant_name: str
    claim_amount: float = Field(..., gt=0)
    claim_status: Optional[ClaimStatusEnum] = ClaimStatusEnum.PENDING
    fraud_flag: Optional[bool] = False
    claim_date: datetime
    description: Optional[str] = None
    

class ClaimCreate(ClaimBase):
    policy_number: str = Field(..., example="POL123456")
    claimant_name: str = Field(..., example="John Doe")
    claim_amount: float = Field(..., gt=0, example=1500.75)
    claim_date: datetime = Field(..., example="2024-03-15T10:00:00Z")
    description: Optional[str] = Field(None, example="Accident on freeway")
    claim_status: Optional[ClaimStatusEnum] = ClaimStatusEnum.PENDING
    fraud_flag: Optional[bool] = False

class ClaimUpdate(ClaimBase):
    claim_amount: Optional[float] = None
    description: Optional[str] = None
    claim_status: Optional[ClaimStatusEnum] = None
    fraud_flag: Optional[bool] = None

class claimResponse(ClaimBase):
    id: UUID
    created_at: datetime

    class Config:
        orm_mode = True
    