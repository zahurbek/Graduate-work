import pytest


@pytest.mark.usefixtures("test_failed_check")
class TestChangeUsername:

    def test_change_username(self, open_site, main_page, settings_page, sql_service):
        user_email = "tushkanchik1090@gmail.com"
        expected_username = "Andrei"
        main_page.login(user_email, "qazwsxedc123")
        main_page.open_settings_page()
        settings_page.change_username(expected_username)

        username_from_db = sql_service.get_first_name(user_email)

        assert expected_username == username_from_db, \
            f"Current name: {username_from_db}Expected name: {expected_username} "
