import math
from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape


class UserTasks(TaskSet):
    host = "https://reqres.in"

    @task
    def get_users(self):
        res = self.client.get("/api/users?page=2")
        print("==================== test running ==================")
        # print(res.text)
        # print(res.status_code)
        # print(res.headers)


class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    tasks = [UserTasks]


class StepLoadShape(LoadTestShape):
    """
    A step load shape
    Keyword arguments:
        step_time -- Time between steps
        step_load -- User increase amount at each step
        spawn_rate -- Users to stop/start per second at every step
        time_limit -- Time limit in seconds
    """

    step_time = 3
    step_load = 1
    spawn_rate = 2
    time_limit = 12

    def tick(self):
        run_time = self.get_run_time()
        print("=============================>>>>>> run_time: ", run_time)

        if run_time > self.time_limit:
            return None

        current_step = math.floor(run_time / self.step_time) + 1
        print("=============================>>>>>> current_step: ", current_step)
        print("=============================>>>>>> self.step_time: ", self.step_time)
        return current_step * self.step_load, self.spawn_rate
