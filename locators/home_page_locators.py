from selenium.webdriver.common.by import By

class HomePageLocators:

    header = (By.XPATH, '//div[contains(@class, "Home_Header__iJKdX")]')

    faq = (By.XPATH, '//div[contains(@class, "Home_FAQ")]')

    #  Вопросы в разделе "Вопросы о важном"
    faq_item_question = {
        1: [By.XPATH, '//div[@id="accordion__heading-0"]/parent::div'],
        2: [By.XPATH, '//div[@id="accordion__heading-1"]/parent::div'],
        3: [By.XPATH, '//div[@id="accordion__heading-2"]/parent::div'],
        4: [By.XPATH, '//div[@id="accordion__heading-3"]/parent::div'],
        5: [By.XPATH, '//div[@id="accordion__heading-4"]/parent::div'],
        6: [By.XPATH, '//div[@id="accordion__heading-5"]/parent::div'],
        7: [By.XPATH, '//div[@id="accordion__heading-6"]/parent::div'],
        8: [By.XPATH, '//div[@id="accordion__heading-7"]/parent::div']
    }

    #  Ответы в разделе "Вопросы о важном"
    faq_item_answer = {
        1: (By.XPATH, '//div[@id="accordion__panel-0"]'),
        2: (By.XPATH, '//div[@id="accordion__panel-1"]'),
        3: (By.XPATH, '//div[@id="accordion__panel-2"]'),
        4: (By.XPATH, '//div[@id="accordion__panel-3"]'),
        5: (By.XPATH, '//div[@id="accordion__panel-4"]'),
        6: (By.XPATH, '//div[@id="accordion__panel-5"]'),
        7: (By.XPATH, '//div[@id="accordion__panel-6"]'),
        8: (By.XPATH, '//div[@id="accordion__panel-7"]')
    }

    # Кнопка "Заказать" в разделе "Как это работает"
    button_order_main_page = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    # Кнопка "Заказать" в шапке сайта
    button_order_header = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')

    header_scooter_logo = (By.XPATH, '//a[@href="/" and contains(@class, "Header_LogoScooter")]')
    header_yandex_logo = (By.XPATH, '//a[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
    title_page = (By.TAG_NAME, 'title')


    # Кнопка "Принять куки"
    cookie_button = (By.ID, 'rcc-confirm-button')


