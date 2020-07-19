from locust import HttpUser, SequentialTaskSet, task, between, events
import time
import json

class MyTaskSet(SequentialTaskSet):
    
    @task
    def list_of_users(self):
        h={'Content-Type': 'application/json'}
        chosen_page = '1'
        response = self.client.get("/users?page={chosen_page!s}".format(**locals()), headers=h)
        json_var = response.json()
        print("List of users status code: ", response.status_code)
        print(json_var)
        assert response.status_code == 200

    @task
    def successfully_login(self):
        successfully_payload = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
        h={'Content-Type': 'application/json'}
        response = self.client.post("/login", data=json.dumps(successfully_payload), headers=h)
        json_var = response.json()
        print("Successfully login status code: ", response.status_code)
        print(json_var)
        assert response.status_code == 200

    @task
    def unsuccessfully_login(self):
        unsuccessfully_payload = {"email": "eve.holt@reqres.in"}
        h={'Content-Type': 'application/json'}
        response = self.client.post("/login", data=json.dumps(unsuccessfully_payload), headers=h)
        json_var = response.json()
        print("Unsuccessfully login status code: ", response.status_code)
        print(json_var)
        assert response.status_code == 400

    @task
    def update_user(self):
        update_payload = {"name": "morpheus", "job":"zion resident"}
        h={'Content-Type': 'application/json'}
        response = self.client.put("/users", data=json.dumps(update_payload), headers=h)
        json_var = response.json()
        print("Update user status code: ", response.status_code)
        print(json_var)
        assert response.status_code == 200

    @task
    def create_user(self):
        create_payload = {"name": "aiana", "job":"singer"}
        h={'Content-Type': 'application/json'}
        response = self.client.post("/users", data=json.dumps(create_payload), headers=h)
        json_var = response.json()
        print("Create user status code: ", response.status_code)
        print(json_var)
        assert response.status_code == 201
    
class MyUser(HttpUser):
    tasks = [MyTaskSet]
    wait_time = between(5, 20)