from nautobot.apps.jobs import Job, register_jobs

class DummyJob(Job):
    class Meta:
        name = "DummyJob"
        description = "Verify working job sync"
    def run(self):
        self.logger.info("Job output 1")
        self.logger.info("Job output 2")
        return "Success!"

register_jobs(DummyJob)