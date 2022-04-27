import pytest

initial_quantity = 1
name_product = "Blue Duck"
set_quantity = 3


@pytest.fixture(scope="session")
def setup_for_basket(open_site, main_page, product_page, basket_page):
    main_page.select_product(name_product)
    product_page.add_product_to_basket(initial_quantity)
    basket_page.open()
    basket_page.set_quantity_product(set_quantity)


@pytest.mark.usefixtures("test_failed_check", "setup_for_basket")
class TestBasket:

    def test_add_product(self, basket_page):
        current_quantity = basket_page.get_current_quantity_product()
        assert current_quantity == set_quantity, \
            f"Current quantity: {current_quantity}. Expected: {set_quantity}"

    def test_price_product(self, basket_page):
        unit_price = basket_page.get_unit_price()
        expected_total_price = unit_price * set_quantity

        current_total_price = basket_page.get_total_price()

        assert expected_total_price == current_total_price, \
            f"Current total price: {current_total_price}. Expected: {expected_total_price}"

    def test_clear_basket(self, basket_page):
        basket_page.clear_basket()
        assert basket_page.is_basket_empty(), "Basket not empty"
