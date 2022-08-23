import time

from locust import User, task, constant_pacing
import time


class MyUser(User):
    wait_time = constant_pacing(4)  # this will add delay of 4 second for each request irrespective of the time it
    # takes to run If the sleep time is more than it wll skip the constant pacing time and it will wait until thte
    # task is finished

    @task
    def launch(self):
        time.sleep(1)
        print("Constant pacing demo")
