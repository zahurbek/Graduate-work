import os
import shutil

import allure
import mysql.connector as mysql
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.settings_page import SettingsPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from services.sql_service.sql_service import SQLService
from services.api_service.api_service import ApiService


@pytest.fixture(scope='session')
def chromedriver():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture(scope='session')
def main_page(chromedriver):
    return MainPage(chromedriver)


@pytest.fixture(scope='session')
def product_page(chromedriver):
    return ProductPage(chromedriver)


@pytest.fixture(scope='session')
def basket_page(chromedriver):
    return BasketPage(chromedriver)


@pytest.fixture(scope='session')
def settings_page(chromedriver):
    return SettingsPage(chromedriver)


@pytest.fixture(scope='session')
def sql_connection():
    connection = mysql.connect(host='localhost',
                               user='root',
                               password='',
                               db='litecart')
    yield connection
    connection.close()


@pytest.fixture(scope='session')
def sql_service(sql_connection):
    return SQLService(sql_connection)


@pytest.fixture(scope='session')
def open_site(chromedriver):
    chromedriver.get("http://localhost/litecart/en/")


@pytest.fixture(scope='session')
def api_service():
    return ApiService()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture()
def test_failed_check(chromedriver, request):
    yield

    if request.node.rep_call.failed:
        test_name = request.node.name
        path = os.path.join(os.getcwd(), "screenshots_of_failed_tests")
        os.mkdir(path)
        allure.attach(chromedriver.save_screenshot(os.path.join(path, f"{test_name}.png")))


@pytest.fixture(scope="session", autouse=True)
def delete_temp_folders():
    my_dir = os.path.join(os.getcwd(), "screenshots_of_failed_tests")
    try:
        shutil.rmtree(my_dir)
    except OSError:
        pass

