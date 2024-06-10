import time


from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC

#from graphQLRequests.requests_1.clining_products import Clining
from .general import General
from .general import Helper






# class MocksUrls(General, Helper):

# class CliningData(Clining):
#
#     def clining_etariff(self):
#         clg = Clining()
#         clg.failProductOrder()
#         clg.cancelProductOrder()
#         clg.terminateProduct()

class Common(General, Helper):

    def access_request(self):
        selector = self.browser.find_element(*CommonLocators.TEXT_ACCESS_REQUEST)
        #time.sleep(1)
        WDW(self.browser, 5).until(EC.visibility_of_element_located((selector)))
        selector = self.browser.find_element(*CommonLocators.BUTTON_ACCESS_YES)
        selector.click()

    def authorization(self, number, kod):
        self.enter_number(number)
        self.enter_kod(kod)
        # При переключении на продлайк возникает дополнительный шаг "Нажать кнопку Пропустить"
        self.push_button_pass()

    def click_photo_account(self):
        time.sleep(1)
        selector = self.browser.find_element(*CommonLocators.PHOTO_ACCOUNT)
        WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))).click()

    def click_exit(self):
        selector = self.browser.find_element(*CommonLocators.BUTTON_EXIT)
        WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))).click()

    def confirm_exit(self):
        selector = self.browser.find_element(*CommonLocators.CONFIRM_EXIT)
        WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))).click()

    def enter_kod(self, kod):
        selector = CommonLocators.FIELD_ENTER_KOD
        text = kod
        self.past_text(self, selector, text)
        # На проде после ввода пароля необходимо нажать кнопку Далее
        # selector = self.browser.find_element(*CommonLocators.BUTTON_NEXT)
        # selector.click()

    def enter_number(self, number):
        selector = CommonLocators.FIELD_ENTER_NUMBER
        text = number
        self.past_text(self, selector, text)
        selector = self.browser.find_element(*CommonLocators.BUTTON_NEXT)
        selector.click()

    def push_button_continue_checkout(self):
        selector = self.browser.find_element(*CommonLocators.BUTTON_BUY_CONTINUE)
        WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))).click()

    def push_button_pass(self):
        time.sleep(1)
        if self.check_exists_element(*CommonLocators.BUTTON_PASS) == True:
            selector = self.browser.find_element(*CommonLocators.BUTTON_PASS)
            # WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))).click()
            selector.click()
        else:
            pass

    def should_be_button_continue_checkout(self):
        # time.sleep(0.5)
        selector = self.browser.find_element(*CommonLocators.BUTTON_BUY_CONTINUE)
        WDW(self.browser, 5).until(EC.element_to_be_clickable((selector))) #.click()
        assert self.check_exists_element(*CommonLocators.BUTTON_BUY_CONTINUE), "Кнопка 'Продолжить оформление' не отображается"

    def should_be_error_personal_offer(self):
        text_error = " Ошибка при получении параметров персонального предложения "
        selector = self.browser.find_element(*CommonLocators.ERROR_401)
        error = selector.get_attribute('text')
        assert error==text_error, "Ошибка авторизации"

    def should_be_photo_account(self):
        #self.browser.navigate().refresh()
        time.sleep(7)
        selector = self.browser.find_element(*CommonLocators.PHOTO_ACCOUNT)
        WDW(self.browser, 5).until(EC.visibility_of((selector)))
        assert self.check_exists_element(*CommonLocators.PHOTO_ACCOUNT), "Абонент не зашел в авторизованную зону"
