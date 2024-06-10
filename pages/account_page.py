import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

from .helpers import Helpers
from ..common_data.timeouts import Timeouts


class AccountLocators:
    BUTTON_NEXT = (By.XPATH, '//*[text() = "Далее"]')
    BUTTON_PASS = (By.XPATH, '//*[text() = "Пропустить"]')
    FIELD_ENTER_CODE = (By.CSS_SELECTOR, 'input[name="otp"]')
    FIELD_ENTER_NUMBER = (By.CSS_SELECTOR, 'input[name="login"]')
    # PHOTO_ACCOUNT = (By.CSS_SELECTOR, 'img[alt = "Фото аккаунта"]')


class AccountPage(Helpers):
    def __init__(self, browser):
        self.browser = browser

    def authorization(self, number, code):
        self.enter_number(number)
        self.enter_code(code)
        # При переключении на продлайк возникает дополнительный шаг "Нажать кнопку Пропустить"
        self.push_button_pass()

    def enter_code(self, code):
        selector = AccountLocators.FIELD_ENTER_CODE
        text = code
        self.past_text(self, selector, text)
        # На проде после ввода пароля необходимо нажать кнопку Далее
        if self.check_exists_element(*AccountLocators.BUTTON_NEXT) == True:
            selector = self.browser.find_element(*AccountLocators.BUTTON_NEXT)
            WDW(self.browser, Timeouts.TIMEOUT_5).until(EC.element_to_be_clickable((selector))).click()
        else:
            pass

    def enter_number(self, number):
        selector = AccountLocators.FIELD_ENTER_NUMBER
        text = number
        self.past_text(self, selector, text)
        selector = self.browser.find_element(*AccountLocators.BUTTON_NEXT)
        selector.click()

    def push_button_pass(self):
        time.sleep(1)
        if self.check_exists_element(*AccountLocators.BUTTON_PASS) == True:
            selector = self.browser.find_element(*AccountLocators.BUTTON_PASS)
            WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))).click()
        else:
            pass

    def should_be_photo_account(self):
        # баг с кнопкой Войти на стейдже
        # self.browser.navigate().refresh()
        # time.sleep(7)
        # selector = self.browser.find_element(*AccountLocators.PHOTO_ACCOUNT)
        # WDW(self.browser, 5).until(EC.visibility_of((selector)))
        # assert self.check_exists_element(*AccountLocators.PHOTO_ACCOUNT), "Абонент не зашел в авторизованную зону"
        pass

# acp = AccountPage(browser=browser)
