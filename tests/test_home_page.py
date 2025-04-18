import allure
from pages.home_page import HomePage
from conftest import driver
from data import TestData
import pytest


class TestFaq:

    @allure.title('"Вопросы о важном"')
    @allure.description('Проверка текста ответов')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_answer_faq)
    def test_click_faq_expand_icons_text_is_expected(self, driver, question_number, expected_answer):
        home_page = HomePage(driver)

        home_page.wait_visibility_cookie()
        home_page.close_cookie_window()

        home_page.scroll_to_faq()
        home_page.wait_faq_items_question_is_visible(question_number)
        home_page.click_faq_item(question_number)
        home_page.wait_faq_items_answers_is_visible(question_number)
        assert home_page.get_text_answer_items_is_displayed(question_number) == expected_answer