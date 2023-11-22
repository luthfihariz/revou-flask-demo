from core.job.constants import JobApplicationStatus
from dataclasses import dataclass

@dataclass
class JobDomain:
    id: int
    title: str
    employer: str
    description: str

@dataclass
class JobApplicationDomain:
    id: int
    user_id: int
    job_id: int
    status: JobApplicationStatus