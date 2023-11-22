from injector import Module, singleton, Binder
from core.job.ports import IJobAccessor, IJobApplicationAccessor
from infrastructure.job.adapters import JobAccessor, JobApplicationAccessor

class JobModule(Module):
    def configure(self, binder: Binder) -> None:
        binder.bind(IJobAccessor, to=JobAccessor, scope=singleton)
        binder.bind(IJobApplicationAccessor, to=JobApplicationAccessor, scope=singleton)