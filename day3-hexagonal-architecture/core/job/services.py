from injector import inject
from core.job.ports import IJobAccessor, IJobApplicationAccessor
from core.user.ports import IUserAccessor

class JobService():

    @inject
    def __init__(self, 
                 job_accessor: IJobAccessor,
                 job_application_accessor: IJobApplicationAccessor,
                 user_accessor: IUserAccessor,
                 ) -> None:
        self.job_accessor = job_accessor
        self.job_application_accessor = job_application_accessor
        self.user_accessor = user_accessor

    def create_job(self, title:str, employer:str, description:str):
        pass

    def get_job_list(self):
        return self.job_accessor.get_all()
    
    def apply_job(self, user_id: int, job_id: int):
        job_application = self.job_application_accessor.create(user_id, job_id)

        user = self.user_accessor.get_by_id(user_id)
        job = self.job_accessor.get_by_id(job_id)

        return {
            'id': job_application.id,
            'status': job_application.status,
            'job_title': job.title,
            'username': user.username,
        }