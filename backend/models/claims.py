
import uuid
from sqlalchemy import Boolean, Column, Float, String, TIMESTAMP, Enum as SQLEnum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text
from sqlalchemy.orm import relationship

from database.enums import ClaimStatusEnum
from database.session import Base



class Claim(Base):
    __tablename__ = "claims"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    policy_number = Column(String, nullable=False)
    claimant_name = Column(String, nullable=False)
    claim_amount = Column(Float, nullable=False, default=0.0)
    claim_status = Column(SQLEnum(ClaimStatusEnum), name="claimstatusenum", default=ClaimStatusEnum.PENDING)
    fraud_flag = Column(Boolean, default=False)
    claim_date = Column(TIMESTAMP(timezone=True), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    description = Column(String, nullable=True)

    ocr_results = relationship("OCRResult", back_populates="claim")


class OCRResult(Base):

    __tablename__ = "ocr_results"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    claim_id = Column(UUID(as_uuid=True), ForeignKey("claims.id"), nullable=False)
    extracted_text = Column(String, nullable=False)
    document_path = Column(String, nullable=True)
    processed = Column(Boolean, default=False)
    classification = Column(String, nullable=True)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))


    claim = relationship("Claim", back_populates="ocr_results")

