# locust-performance-testing

It’s crucial to have a common definition for the types of performance tests that should be executed against the applications using locust, such as:

Single User Tests: Testing with one active user yields the best possible performance, and response times can be used for baseline measurements.

Load Tests: Understand the behavior of the system under average load, including the expected number of concurrent users performing a specific number of transactions within an average hour.

Peak Load Tests: Understand system behavior under the heaviest anticipated usage for the concurrent number of users and transaction rates.

Endurance (Soak) Tests: Determine the longevity of components, and whether the system can sustain average to a peak load over a predefined duration. Also, monitor memory utilization to detect potential leaks.

Stress Tests: Understand the upper limits of capacity within the system by purposely pushing it to its breaking point.

## Installation
Install the latest python if it's not already installed [python installation guide](https://docs.python-guide.org/starting/install3/osx/).

Install locust ´pip3 install locust´ & verify with ´locust -V´


## GET Example
We have the import statement on top. Then we define the user class that will get simulated when the test is running. CitiesNearBy class extends FastHttpUser class since our application is using an HTTP call for the interaction. wait_timeis used to specify how long a simulated user should wait between executing tasks, and the decorator @task is used to identify that the get_cities_nearby method is a task that should get executed by the simulated user.

from locust import FastHttpUser, task, constant

class CitiesNearBy(FastHttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)

    @task    
    def get_cities_nearby(self):
        self.client.get("/api/users?page=2")
        
Do not use zero think time. Make sure that think time in your test is based on real-life conditions. Using zero think time does not provide realistic user simulation and puts an abnormal load on the tested server. However, omitting think time can help you determine bottleneck issues.

## POST Example
Below is a basic example of a post request where a simulated user will be making a post call every one second.

from locust import FastHttpUser, constant, task

class MyReqRes(FastHttpUser):
    host = "https://reqres.in"    
    wait_time = constant(1)

    @task    
    def create_user(self):
        self.client.post("/api/users", data='''{"name": "morpheus",
                "job": "leader"}''')
