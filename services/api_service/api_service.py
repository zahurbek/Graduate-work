import allure
from services.api_service.base_api_service import BaseApiService


class ApiService(BaseApiService):

    @allure.step("Create user")
    def create_user(self, data):
        self.post(data)

    @allure.step("Get info user")
    def get_user_info(self, username):
        return self.get(username)

    @allure.step("Change username")
    def update_user(self, old_username, new_data):
        self.put(old_username, new_data)

    def delete_user(self, username):
        self.delete(username)
