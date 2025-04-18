import allure
from conftest import driver
from pages.home_page import HomePage


class TestLogo:

    @allure.title('Проверка открытия главной страницы "Самокат"')
    def test_logo_scooter_open_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.wait_button_order_in_header_is_visible()
        home_page.click_button_order_in_header()
        home_page.wait_scooter_logo_in_header_is_visible()
        home_page.click_scooter_logo_in_header()
        home_page.wait_header_is_visible()
        assert home_page.check_header_is_displayed()

    @allure.title('Проверка перехода на "Дзен"')
    def test_logo_yandex_open_dzen(self, driver):
        home_page = HomePage(driver)
        home_page.wait_yandex_logo_in_header_is_visible()
        home_page.click_yandex_logo_in_header()
        home_page.switch_next_tab()
        assert home_page.get_page_title() == 'Дзен — платформа для просмотра и создания контента. Вы всегда найдёте здесь то, что подходит именно вам: сотни тысяч авторов ежедневно делятся постами, статьями, видео и короткими роликами'