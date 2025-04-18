import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import TestData


class OrderPage(BasePage):

    @allure.step('Ожидание появления окна куки')
    def wait_visibility_cookie(self):
        self.wait_element_is_visible(OrderPageLocators.cookie_button)

    @allure.step('Закрытие окна куки')
    def close_cookie_window(self):
        self.click_element(OrderPageLocators.cookie_button)

    @allure.step('Клик на станцию метро')
    def select_subway_station(self):
        self.click_element(OrderPageLocators.select_item_in_multiselect)

    @allure.step('Выбор даты заказа')
    def send_keys_date(self):
        self.send_keys_input(OrderPageLocators.date).send_keys(TestData.test_data_one[5])

    @allure.step('Клик по дате заказа')
    def click_on_date_in_calendar(self):
        self.click_element(OrderPageLocators.calendar_item)

    @allure.step('Просмотр отображения кнопки статуса заказа')
    def check_button_status_order_is_displayed(self):
        return self.check_element_is_displayed(OrderPageLocators.button_check_status_order)

    @allure.step('Заполнение формы заказа, первая страница')
    def data_first_form(self, test_data):
        self.wait_element_is_visible(OrderPageLocators.name)
        self.click_element(OrderPageLocators.name)
        self.send_keys_input(OrderPageLocators.name, test_data[0])
        self.click_element(OrderPageLocators.surname)
        self.send_keys_input(OrderPageLocators.surname, test_data[1])
        self.click_element(OrderPageLocators.address)
        self.send_keys_input(OrderPageLocators.address, test_data[2])
        self.click_element(OrderPageLocators.subway_station)
        self.send_keys_input(OrderPageLocators.subway_station, test_data[3])
        self.click_element(OrderPageLocators.select_item_in_multiselect)
        self.click_element(OrderPageLocators.phone_number)
        self.send_keys_input(OrderPageLocators.phone_number, test_data[4])
        self.click_element(OrderPageLocators.button_next)

    @allure.step('Заполнение формы заказа, вторая страница')
    def data_second_form(self, test_data):
        self.wait_element_is_visible(OrderPageLocators.date)
        self.click_element(OrderPageLocators.date)
        self.send_keys_input(OrderPageLocators.date, test_data[5])
        self.click_element(OrderPageLocators.checkbox_grey_color_scooter)
        self.click_element(OrderPageLocators.checkbox_black_color_scooter)
        self.click_element(OrderPageLocators.field_rent_period)
        self.click_element(OrderPageLocators.multiselect_item_rent_period)
        self.click_element(OrderPageLocators.comment)
        self.send_keys_input(OrderPageLocators.comment, test_data[6])
        self.click_element(OrderPageLocators.button_make_order)
        self.wait_element_is_visible(OrderPageLocators.button_confirm_order)
        self.click_element(OrderPageLocators.button_confirm_order)