from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape


class UserTasks(TaskSet):
    host = "https://reqres.in"

    @task(3)
    def get_users(self):
        res = self.client.get("/api/users?page=2")
        # print(res.text)
        # print(res.status_code)
        # print(res.headers)

    @task(1)
    def get_users_invalid(self):
        res = self.client.get("/api/users/invalid?page=2")


class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    tasks = [UserTasks]


class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.
    Keyword arguments:
        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage
        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"duration": 6, "users": 10, "spawn_rate": 10},
        {"duration": 10, "users": 50, "spawn_rate": 10},
        {"duration": 18, "users": 100, "spawn_rate": 10},
        {"duration": 40, "users": 30, "spawn_rate": 10},
        {"duration": 60, "users": 10, "spawn_rate": 10},
        {"duration": 80, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
