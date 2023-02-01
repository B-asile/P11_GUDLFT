from locust import HttpUser, task, between


class User(HttpUser):
    host = "http://127.0.0.1:5000/"

    @task
    def index(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.post("/showSummary", data={"email": "john@simplylift.co"})

    @task
    def book(self):
        self.client.get("/book/Spring Festival/Simply Lift")

    @task
    def purchasePlaces(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": 1
            }
        )

    @task
    def point_display(self):
        self.client.get("/points-display")

    @task
    def logout(self):
        self.client.get("/logout")
