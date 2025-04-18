import allure
from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage


class HomePage(BasePage):


    @allure.step('Ожидание появления окна куки')
    def wait_visibility_cookie(self):
        self.wait_element_is_visible(HomePageLocators.cookie_button)

    @allure.step('Закрытие окна куки')
    def close_cookie_window(self):
        self.click_element(HomePageLocators.cookie_button)

    @allure.step('Ожидание загрузки кнопки "Заказать" в хедере')
    def wait_button_order_in_header_is_visible(self):
        self.wait_element_is_visible(HomePageLocators.button_order_header)

    @allure.step('Клик по кнопке заказа в хедере')
    def click_button_order_in_header(self):
        self.click_element(HomePageLocators.button_order_header)

    @allure.step('Ожидание загрузки лого "Самокат"')
    def wait_scooter_logo_in_header_is_visible(self):
        self.wait_element_is_visible(HomePageLocators.header_scooter_logo)

    @allure.step('Ожидание загрузки лого "Яндекс"')
    def wait_yandex_logo_in_header_is_visible(self):
        self.wait_element_is_visible(HomePageLocators.header_yandex_logo)

    @allure.step('Клик по лого "Самокат"')
    def click_scooter_logo_in_header(self):
        self.click_element(HomePageLocators.header_scooter_logo)

    @allure.step('Клик по лого "Яндекс"')
    def click_yandex_logo_in_header(self):
        self.click_element(HomePageLocators.header_yandex_logo)

    @allure.step('Ожидание загрузки заголовка')
    def wait_header_is_visible(self):
        self.wait_element_is_visible(HomePageLocators.header)

    @allure.step('Проверка заголовка')
    def check_header_is_displayed(self):
        return self.check_element_is_displayed(HomePageLocators.header)

    @allure.step('Скролл до "Вопросы о важном"')
    def scroll_to_faq(self):
        self.scroll_to_element(HomePageLocators.faq)

    @allure.step('Ожидание загрузки в "Вопросы о важном"')
    def wait_faq_items_question_is_visible(self, data):
        self.wait_element_is_visible(HomePageLocators.faq_item_question[data])

    @allure.step('Клик на номер вопроса в "Вопросы о важном"')
    def click_faq_item(self, data):
        self.click_element(HomePageLocators.faq_item_question[data])

    @allure.step('Ожидание загрузки ответа в "Вопросы о важном"')
    def wait_faq_items_answers_is_visible(self, data):
        self.wait_element_is_visible(HomePageLocators.faq_item_answer[data])

    @allure.step('Текст ответа в "Вопросы о важном"')
    def get_text_answer_items_is_displayed(self, data):
        return self.get_text_at_element(HomePageLocators.faq_item_answer[data])