from locust import HttpUser, constant, task, constant_throughput, LoadTestShape


class MyReqRes(HttpUser):
    host = "https://reqres.in"
    wait_time = constant_throughput(5)

    @task
    def get_users(self):
        res = self.client.get("/api/users?page=2")
        print(res.text)
        print(res.status_code)
        print(res.headers)

    @task
    def create_user(self):
        self.client.post("/api/users", data='''{
        "name": "morpheus",
        "job": "leader"
        }''')


class MyCustomShape(LoadTestShape):
    time_limit = 600
    spawn_rate = 20

    def tick(self):
        run_time = self.get_run_time()

        if run_time < self.time_limit:
            # User count rounded to nearest hundred.
            user_count = round(run_time, -2)
            return (user_count, self.spawn_rate)

        return None
