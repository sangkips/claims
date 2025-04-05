
import uuid
from sqlalchemy import Boolean, Column, Float, String, TIMESTAMP, Enum as SQLEnum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text



from database.enums import ClaimStatusEnum
from database.session import Base



class Claim(Base):
    __tablename__ = "claims"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    policy_number = Column(String, nullable=False)
    claimant_name = Column(String, nullable=False)
    claim_amount = Column(Float, nullable=False, default=0.0)
    claim_status = Column(SQLEnum, name="claimstatusenum", default=ClaimStatusEnum.PENDING), 
    fraud_flag = Column(Boolean, default=False)
    claim_date = Column(TIMESTAMP(timezone=True), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    description = Column(String, nullable=True)

