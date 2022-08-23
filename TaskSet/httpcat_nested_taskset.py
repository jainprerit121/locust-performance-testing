import random

from locust import TaskSet, task, constant, HttpUser


class MyHttpCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("get status 200")

    @task
    def get_random_status(self):
        status_codes = [100, 200, 300, 101, 102, 402, 403, 401]
        random_url = "/" + str(random.choice(status_codes))
        res = self.client.get(random_url)

        print("random http status")

    @task
    class MyAnotherHttpCat(TaskSet):
        @task
        def get_500_status(self):
            self.client.get("/500")
            print("500 http status")
            self.interrupt(reschedule=False)


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHttpCat]
    wait_time = constant(1)
