from enum import Enum

class ClaimStatusEnum(str, Enum):
    """Enumeration for claim status."""
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    UNDER_REVIEW = "Under Review"