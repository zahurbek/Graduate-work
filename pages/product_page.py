import allure

from pages.base_page import BasePage


class ProductPage(BasePage):
    QUANTITY_INPUT_LOCATOR = "//input[@name='quantity']"
    ADD_TO_CART_BUTTON_LOCATOR = "//button[@value='Add To Cart']"
    CHANGE_SIZE_BUTTON_LOCATOR = "//select[contains(@name,'Size')]"
    SIZE_LOCATOR = "//option[@value='{}']"
    QUANTITY_IN_BASKET_LOCATOR = "//span[@class='quantity' and text()='{}']"
    SIZE_BUTTON_LOCATOR = "//select[contains(@name,'Size')]"
    SIZE_NAME_LOCATOR = "//option[@value='{}']"

    @allure.step("Add product to basket")
    def add_product_to_basket(self, quantity, size_duck=None):
        quantity_in_basket_locator = self.QUANTITY_IN_BASKET_LOCATOR.format(quantity)
        self.set_size_duck(size_duck)
        self.set_quantity(self.QUANTITY_INPUT_LOCATOR, quantity)
        self.click(self.ADD_TO_CART_BUTTON_LOCATOR)
        self.wait_loading(quantity_in_basket_locator)

    @allure.step("Select size duck: {size_duck}")
    def set_size_duck(self, size_duck):
        if self.is_element_present(self.SIZE_BUTTON_LOCATOR):
            size_locator = self.SIZE_NAME_LOCATOR.format(size_duck)
            self.click(self.SIZE_BUTTON_LOCATOR)
            self.click(size_locator)
