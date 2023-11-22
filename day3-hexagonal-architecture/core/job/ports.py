from abc import ABC, abstractmethod
from typing import List
from core.job.models import JobApplicationDomain, JobDomain

class IJobAccessor(ABC):

    @abstractmethod
    def get_all(self) -> List[JobDomain]:
        raise NotImplementedError
    
    @abstractmethod
    def get_by_id(self, user_id: int) -> JobDomain:
        raise NotImplementedError
    

class IJobApplicationAccessor(ABC):

    @abstractmethod
    def create(self, user_id: int, job_id: int) -> JobApplicationDomain:
        raise NotImplementedError