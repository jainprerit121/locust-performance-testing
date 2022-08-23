from locust import SequentialTaskSet, HttpUser, task, constant


class MySequncialTaskSet(SequentialTaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("Status of 200")

    @task
    def get_500_status(self):
        self.client.get("/500")
        print("Status of 500")


class MyLoadTest(HttpUser):
    host = "http://http.cat"
    tasks = [MySequncialTaskSet]
    wait_time = constant(1)
