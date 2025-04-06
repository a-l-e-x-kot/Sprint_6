import allure
import pytest
from conftest import driver
from pages.order_page import OrderPage
from locators.home_page_locators import HomePageLocators
from data import *


class TestOrderPage:

    @allure.title('Позитивный сценарий оформления заказа')
    @allure.description('Проверка оформления заказа из двух входных точек')
    @pytest.mark.parametrize('button, test_data', [(HomePageLocators.button_order_header, TestData.test_data_one), (HomePageLocators.button_order_main_page, TestData.test_data_two)])
    def test_order_all_fields_success(self, driver, button, test_data):
        order_page = OrderPage(driver)
        order_page.scroll_to_element(button)
        order_page.wait_element_is_visible(button)
        order_page.click_element(button)
        order_page.data_first_form(test_data)
        order_page.data_second_form(test_data)
        assert order_page.check_button_status_order_is_displayed()