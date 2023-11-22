from enum import Enum

class JobApplicationStatus(Enum):
    APPLIED = 'APPLIED'
    INTERVIEWED = 'INTERVIEWED'
    OFFER_ACCEPTED = 'OFFER_ACCEPTED'
    REJECTED = 'REJECTED'