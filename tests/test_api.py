import pytest

data = {
    "id": 4,
    "username": "zahurbek",
    "firstName": "Yury",
    "lastName": "Zhernosek",
    "email": "urazernosek@gmail.com",
    "password": "1111",
    "phone": "+37539003792",
    "userStatus": 0
}
initial_username = data["username"]
new_username = "pulman"


@pytest.fixture(scope='session')
def delete_user(api_service):
    yield
    api_service.delete_user(new_username)


@pytest.mark.usefixtures("delete_user")
class TestApi:

    def test_create_user(self, api_service):
        api_service.create_user(data)
        actual_user = api_service.get_user_info(initial_username)
        assert actual_user == data, "Found another user"

    def test_change_username(self, api_service):
        new_data = data.copy()
        new_data["username"] = new_username
        api_service.update_user(initial_username, new_data)
        actual_user = api_service.get_user_info(new_username)
        assert actual_user == new_data, "Found another user"
