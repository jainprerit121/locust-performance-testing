from locust import User, constant, task


class TestOnStartNStop(User):
    wait_time = constant(2)

    def on_start(self):
        print("on start")

    def on_stop(self):
        print("on stop")

    @task
    def sample_task(self):
        print("task run")
