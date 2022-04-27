import re
import allure

from pages.base_page import BasePage


class BasketPage(BasePage):
    QUANTITY_INPUT_LOCATOR = "//input[@name='quantity']"
    UPDATE_BUTTON_LOCATOR = "//button[@value='Update']"
    UNIT_PRICE_LOCATOR = "//td[@class='unit-cost']"
    TOTAL_PRICE_LOCATOR = "//tr[@class='footer']//td[2]//strong"
    REMOVE_BUTTON_LOCATOR = "//button[@value='Remove']"
    PRODUCT_IN_BASKET_LOCATOR = "//form[@name='cart_form']"
    BASKET_BUTTON_LOCATOR = "//div[@id='cart']"
    WAITING_QUANTITY_LOCATOR = "//input[@value='{}']"

    @allure.step("Set quantity product")
    def set_quantity_product(self, quantity):
        new_quantity_locator = self.WAITING_QUANTITY_LOCATOR.format(quantity)
        self.set_quantity(self.QUANTITY_INPUT_LOCATOR, quantity)
        self.click(self.UPDATE_BUTTON_LOCATOR)
        self.wait_loading(new_quantity_locator)

    def get_current_quantity_product(self):
        attribute = self.get_attribute(self.QUANTITY_INPUT_LOCATOR, "value")
        return int(attribute)

    def get_unit_price(self):
        return self._get_price(self.UNIT_PRICE_LOCATOR)

    def get_total_price(self):
        return self._get_price(self.TOTAL_PRICE_LOCATOR)

    def _get_price(self, locator):
        price = self.get_text(locator)
        price = re.findall("[0-9.]+", price)
        return float(price[0])

    @allure.step("Clear basket")
    def clear_basket(self):
        items_count = self.get_elements_count(self.REMOVE_BUTTON_LOCATOR)
        for element in range(items_count):
            self.click(self.REMOVE_BUTTON_LOCATOR)

    def is_basket_empty(self):
        return self.is_element_present(self.PRODUCT_IN_BASKET_LOCATOR)

    @allure.step("Open basket")
    def open(self):
        self.click(self.BASKET_BUTTON_LOCATOR)
