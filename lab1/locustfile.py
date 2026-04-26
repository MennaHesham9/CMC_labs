from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(0.1, 0.5)

    @task
    def test_home(self):
        self.client.get("/")