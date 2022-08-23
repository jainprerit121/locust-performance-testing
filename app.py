from locust import User, task, constant


class MyFirstClass(User):
    # pass #just to bypass
    weight = 2
    wait_time = constant(1)

    @task
    def launch(self):
        print("launching the URL")

    @task
    def search(self):
        print("searching")


class MySecondClass(User):
    # pass #just to bypass

    weight = 2
    wait_time = constant(1)

    @task
    def launch1(self):
        print("launching the URL from second")

    @task
    def search1(self):
        print("searching from second")
