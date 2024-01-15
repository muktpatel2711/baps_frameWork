from locust import HttpUser,task,between

class MyUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def my_task(self):
        login_payload = {

            'username': 'hiteshpatel1487',
            'password': 'Ims@0503 '

        }
        response = self.client.post ("/",json = login_payload)
        if response.status_code == 200:
            print("Login successful")
        else:
            print("Login failed")