import json
import requests


headers = {'Content-Type': 'application/json'}
expected_status_code = 200


class BaseApiService:

    BASE_USER_URL = "https://petstore.swagger.io/v2/user/"

    def post(self, data):
        json_data = json.dumps(data)
        response = requests.request("POST", self.BASE_USER_URL, data=json_data, headers=headers)
        assert response.status_code == expected_status_code,\
            f"Expected status code: {expected_status_code}. Current status code: {response.status_code}"

    def get(self, username):
        response = requests.request("GET", self.BASE_USER_URL + username)
        assert response.status_code == expected_status_code,\
            f"Expected status code: {expected_status_code}. Current status code: {response.status_code}"
        return json.loads(response.text)

    def put(self, old_username, data):
        json_data = json.dumps(data)
        response = requests.request("PUT", self.BASE_USER_URL + old_username, data=json_data, headers=headers)
        assert response.status_code == expected_status_code,\
            f"Expected status code: {expected_status_code}. Current status code: {response.status_code}"

    def delete(self, username):
        requests.request("DELETE", self.BASE_USER_URL + username)
