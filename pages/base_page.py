import os

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def _get_locator_by_type(self, locator):
        prefixes = ["//", "./", "("]
        result = locator.startswith(tuple(prefixes))
        if result:
            return By.XPATH
        return By.CSS_SELECTOR

    def click(self, locator):
        element = self._find_element(locator)
        element.click()

    def open_url(self, url):
        self.driver.get(url)

    def enter_text(self, locator, text):
        element = self._find_element(locator)
        element.send_keys(text)

    def get_text(self, locator):
        element = self._find_element(locator)
        return element.text

    def clear_field(self, locator):
        element = self._find_element(locator)
        element.clear()

    def is_element_present(self, locator):
        try:
            self._find_element(locator, 2)
            return True
        except TimeoutException:
            return False

    def _wait_for_element_present(self, locator, time_out_sec=10):
        locator_by_type = self._get_locator_by_type(locator)

        element = WebDriverWait(self.driver, time_out_sec).until(
            EC.presence_of_element_located((locator_by_type, locator)))

        return element

    def _wait_for_elements_present(self, locator, time_out_sec=10):
        locator_by_type = self._get_locator_by_type(locator)

        elements = WebDriverWait(self.driver, time_out_sec).until(
            EC.presence_of_all_elements_located((locator_by_type, locator)))

        return elements

    def _find_element(self, locator, time_out_sec=5):
        return self._wait_for_element_present(locator, time_out_sec)

    def _find_elements(self, locator, time_out_sec=5):
        return self._wait_for_elements_present(locator, time_out_sec)

    def get_attribute(self, locator, attribute):
        element = self._find_element(locator)
        return element.get_attribute(attribute)

    def set_quantity(self, input_locator, text):
        self.clear_field(input_locator)
        self.enter_text(input_locator, text)

    def wait_loading(self, locator):
        self._wait_for_element_present(locator)

    def get_list_elements(self, locator):
        return self._find_elements(locator)

    def get_elements_count(self, locator):
        return len(self.get_list_elements(locator))
