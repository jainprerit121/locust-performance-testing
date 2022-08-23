import time

from locust import User, task, constant, between, constant_pacing


class MyUser(User):
    wait_time = constant(1)  # This will inject one-second delay between each req with additional execution time of task

    # wait_time = between(2, 5)  # this will add random delay between to 2 to 5, min=2 & max=5 with additional execution time of task

    @task
    def launch(self):
        time.sleep(3)
        print("This will inject 1 second delay")
