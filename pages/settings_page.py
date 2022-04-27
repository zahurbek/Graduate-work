import allure

from pages.base_page import BasePage


class SettingsPage(BasePage):

    FIRST_NAME_INPUT_LOCATOR = "//input[@name='firstname']"
    SAVE_BUTTON_LOCATOR = "//button[@name='save']"

    @allure.step("Change username")
    def change_username(self, first_name):
        self.set_quantity(self.FIRST_NAME_INPUT_LOCATOR, first_name)
        self.click(self.SAVE_BUTTON_LOCATOR)
