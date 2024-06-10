import time
import requests
import allure
from selenium.common import NoSuchElementException
from selenium.common import ElementClickInterceptedException


class Helpers:

    def check_exists_element(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def check_no_exists_element(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return True
        return False

    def check_unclickable_element(self, selector):
        try:
            selector.click()
        except ElementClickInterceptedException:
            return True
        return False

    def choose_from_list(self, selector, selector_list):
        field = self.browser.find_element(*selector)
        field.click()
        web_element = self.browser.find_element(*selector_list)
        web_element.click()

    def confirm_alert(self):
        time.sleep(0.5)
        alert = self.browser.switch_to.alert
        alert.accept()

    def confirm_del(self, selector):
        selector = self.browser.find_element(*selector)
        selector.click()

    def fined(self, howcell, whatcell, how, what):
        cell = self.browser.find_elements(howcell, whatcell)
        text = self.browser.find_element(how, what)
        i = 0
        while cell[i] != text:
            i += 1
        return i

    def past_text(self, browser, selector, text):
        field = self.browser.find_element(*selector)
        field.click()
        field.clear()
        field.send_keys(text)

    def scroll(self):
        self.browser.execute_script("window.scrollBy(0,500)", "")

    def turn_pages(self, browser, recording, selector):
        while not self.check_exists_element(*recording):
            if self.check_exists_element(*selector):
                selector = browser.driver.find_element(*selector)
                selector.click()
                if self.check_exists_element(*recording):
                    return
            else:
                return

    def cancel_order(self):
        with allure.step("Отмена заказа"):
            url = 'https://ep-ordering.mts-corp.ru/order/graphql/'
            with open('tests/test_swagger_be/pages/data/cancel_product_order.txt') as f:
                mutation_cancel_product_order = f.read().replace('\n', '').replace('\r', '')
        response = requests.post(url, json={'query': mutation_cancel_product_order},
                                 verify='certificates/class2root.crt')
        with allure.step("Проверка статуса ответа"):
            status_code_response = response.status_code
            assert response.status_code == 200, f'Что-то пошло не так, статус ответа {status_code_response}'

    def send_request(self, method, url, cookies=None, data=None, json=None, headers=None, verify=None):
        if headers is None:
            headers = {}
        if method == 'GET':
            response = requests.get(url, cookies=cookies, headers=headers, verify=verify)
            allure.attach(response.content, 'RESPONSE', allure.attachment_type.JSON)
        elif method == 'POST':
            response = requests.post(url, cookies=cookies, data=data, json=json, headers=headers, verify=verify)
            allure.attach(response.content, 'RESPONSE', allure.attachment_type.JSON)
        return response

    def parse_query_data(self,file):
        with open(file) as f:
            query_data = f.read().replace('\n', '').replace('\r', '')
            return query_data
