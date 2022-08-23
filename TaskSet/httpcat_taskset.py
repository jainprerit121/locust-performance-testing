import random

from locust import TaskSet, task, constant, HttpUser


class MyHttpCat(TaskSet):

    @task
    def get_status(self):
        self.client.get("/200")
        print("get status 200")
        #self.interrupt()  # interupt to run both the class as part of task list
        self.interrupt(reschedule=False)  # interupt to run both the class as part of task list and it will add some wait time between both classes

    @task
    def get_random_status(self):
        status_codes = [100, 200, 300, 101, 102, 402, 403, 401]
        random_url = "/" + str(random.choice(status_codes))
        res = self.client.get(random_url)

        print("random http status")
        self.interrupt(reschedule=False)


@task
class MyAnotherHttpCat(TaskSet):
    @task
    def get_500_status(self):
        self.client.get("/500")
        print("500 http status")
        #self.interrupt()
        self.interrupt(reschedule=False)  # interupt to run both the class as part of task list and it will add some wait time between both classes


class MyLoadTest(HttpUser):
    host = "https://http.cat"
    tasks = [MyHttpCat, MyAnotherHttpCat]
    wait_time = constant(1)
