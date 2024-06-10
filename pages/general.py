import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class GeneralLocators():
    CONFIRM_DEL_BUTTON = (By.CSS_SELECTOR, 'button.remove-icon.text-white.footer')
    DOCUMENTS = (By.XPATH, '//span[text()="Документы"]')
    TURN_PAGES = (By.XPATH, '//button[text()="›"]')


class General():

    def __init__(self, browser, timeout=10):
        self.browser = browser
        #self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self)


class Helper():
    def __init__(self, browser):
        self.browser = browser

    def check_exists_element(self,how,what):
        try:
           self.browser.find_element(how,what)
           #self.browser.element_is_visible(how, what)
        except NoSuchElementException:
            return False
        return True

    def check_no_exists_element(self, how, what):
        try:
           self.browser.find_element(how,what)
        except NoSuchElementException:
            return True
        return False

    def choose_from_list(self, browser, selector, selector_list):
        field = self.browser.find_element(*selector)
        field.click()
        list = self.browser.find_element(*selector_list)
        list.click()

    def confirm_alert(self):
        time.sleep(0.5)
        alert = self.browser.switch_to.alert
        alert.accept()

    def confirm_del(self):

        selector = self.browser.find_element(*GeneralLocators.CONFIRM_DEL_BUTTON)
        selector.click()

    def fined(self, browser, howcell, whatcell,how, what):
        cell = self.browser.find_elements(howcell, whatcell)
        text = self.browser.find_element(how, what)
        #text.click()
        i = 0
        while cell[i] != text:
            i += 1
            #self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(i)
        return (i)

    def past_text(self, browser, selector, text):
        field = self.browser.find_element(*selector)
        field.click()
        field.clear()
        field.send_keys(text)

    def scroll(self):#, selector,):
        self.browser.execute_script("window.scrollBy(0,500)", "")

    def start_report(self):
        print('Тестовое пространство очищено')

    def turn_pages(self, browser, recording):
        while (self.check_exists_element(*recording) == False):
            if (self.check_exists_element(*GeneralLocators.TURN_PAGES) == True):
                selector = self.browser.find_element(*GeneralLocators.TURN_PAGES)
                selector.click()
                if self.check_exists_element(*recording) == True:
                    return
            else:
                return

