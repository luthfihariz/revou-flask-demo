from abc import ABC, abstractmethod
from typing import List

from core.job.ports import IJobAccessor, IJobApplicationAccessor
from core.job.models import JobDomain,JobApplicationDomain
from infrastructure.job.models import Job, JobApplication
from core.common.utils import ObjectMapperUtil
from infrastructure.db import db

class JobAccessor(IJobAccessor):

    def get_all(self) -> List[JobDomain]:
        jobs = Job.query.all()
        return ObjectMapperUtil.map_array(jobs, JobDomain)

    def get_by_id(self, job_id: int) -> JobDomain:
        job = Job.query.get(job_id)
        return ObjectMapperUtil.map(job, JobDomain)
    


class JobApplicationAccessor(IJobApplicationAccessor):

    def create(self, user_id: int, job_id: int) -> JobApplicationDomain:
        job_app = JobApplication(user_id=user_id, job_id=job_id)
        db.session.add(job_app)
        db.session.commit()

        return ObjectMapperUtil.map(job_app, JobApplicationDomain)