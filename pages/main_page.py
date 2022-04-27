import allure

from pages.base_page import BasePage


class MainPage(BasePage):
    EMAIL_INPUT_LOCATOR = "//input[@name='email']"
    PASSWORD_INPUT_LOCATOR = "//input[@name='password']"
    LOGIN_BUTTON_LOCATOR = "//button[@type='submit']"
    PRODUCT_LOCATOR = "//div[text()= '{}']"
    SETTINGS_PAGE_LOCATOR = "//a[contains(@href,'edit_account')]"

    @allure.step("Login")
    def login(self, email, password):
        self.enter_text(self.EMAIL_INPUT_LOCATOR, email)
        self.enter_text(self.PASSWORD_INPUT_LOCATOR, password)
        self.click(self.LOGIN_BUTTON_LOCATOR)

    @allure.step("Select product")
    def select_product(self, name):
        new_product_locator = self.PRODUCT_LOCATOR.format(name)
        self.click(new_product_locator)

    @allure.step("Open settings page")
    def open_settings_page(self):
        self.click(self.SETTINGS_PAGE_LOCATOR)
