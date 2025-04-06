from selenium.webdriver.common.by import By

class HomePageLocators:

    header = (By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]')

    faq = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')

    #  Вопросы в разделе "Вопросы о важном"
    faq_item_question = {
        1: (By.ID, "accordion__heading-32"),
        2: (By.ID, "accordion__heading-33"),
        3: (By.ID, "accordion__heading-34"),
        4: (By.ID, "accordion__heading-35"),
        5: (By.ID, "accordion__heading-36"),
        6: (By.ID, "accordion__heading-37"),
        7: (By.ID, "accordion__heading-38"),
        8: (By.ID, "accordion__heading-39")
    }

    #  Ответы в разделе "Вопросы о важном"
    faq_item_answer = {
        1: (By.ID, "accordion__panel-32"),
        2: (By.ID, "accordion__panel-33"),
        3: (By.ID, "accordion__panel-34"),
        4: (By.ID, "accordion__panel-35"),
        5: (By.ID, "accordion__panel-36"),
        6: (By.ID, "accordion__panel-37"),
        7: (By.ID, "accordion__panel-38"),
        8: (By.ID, "accordion__panel-39")
    }

    # Кнопка "Заказать" в разделе "Как это работает"
    button_order_main_page = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    # Кнопка "Заказать" в шапке сайта
    button_order_header = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')

    header_scooter_logo = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    header_yandex_logo = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
    title_page = (By.TAG_NAME, 'title')



