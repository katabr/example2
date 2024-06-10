
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class StartUnifiedProductPageLocators:
    BUTTON_DETAILS = (By.CSS_SELECTOR, 'ep-ui-button')
    BUTTON_ORDER = (By.CSS_SELECTOR, 'button[type="button"]')
    SHADOW_ROOT_BUTTON_DETAILS = (By.CSS_SELECTOR, 'wcw-offer-services')
    SHADOW_ROOT2_BUTTON_DETAILS = (By.CSS_SELECTOR, 'div>wcw-service-card')
    SHADOW_ROOT_BUTTON_ORDER = (By.CSS_SELECTOR, 'app-card>wcw-save-offer-settings-button')
    SHADOW_ROOT2_BUTTON_ORDER = (By.CSS_SELECTOR, 'wcw-save-settings-button')
    SHADOW_ROOT3_BUTTON_ORDER = (By.CSS_SELECTOR, 'ep-ui-button')
    SHADOW_ROOT_OPTION = (By.CSS_SELECTOR, 'ep-ui-dialog>h3.dialog-sub-title')


class StartUnifiedProductPage:

    def __init__(self, browser):
        self.browser = browser

    def open_option_details(self):
        shadow_host1 = self.browser.find_element(*StartUnifiedProductPageLocators.SHADOW_ROOT_BUTTON_DETAILS).shadow_root
        shadow_host2 = shadow_host1.find_element(*StartUnifiedProductPageLocators.SHADOW_ROOT2_BUTTON_DETAILS).shadow_root
        selector = shadow_host2.find_element(*StartUnifiedProductPageLocators.BUTTON_DETAILS)
        WDW(self.browser, 10).until(EC.element_to_be_clickable((selector))).click()

    def should_be_clickable_plugging_button(self):
        shadow_host1 = self.browser.find_element(*StartUnifiedProductPageLocators.SHADOW_ROOT_BUTTON_ORDER).shadow_root
        shadow_host2 = shadow_host1.find_element(*StartUnifiedProductPageLocators.SHADOW_ROOT2_BUTTON_ORDER).shadow_root
        shadow_host3 = shadow_host2.find_element(*StartUnifiedProductPageLocators.SHADOW_ROOT3_BUTTON_ORDER).shadow_root
        selector = shadow_host3.find_element(*StartUnifiedProductPageLocators.BUTTON_ORDER)
        active_plug = WDW(self.browser, 5).until(EC.element_to_be_clickable((selector)))
        assert active_plug != None, "Кнопка Оформить заказ для Универсального лендинга продаж монопродукта не активна."

    def should_be_open_option(self):
        shadow_host1 = self.browser.find_element(*StartUnifiedProductPageLocators.SHADOW_ROOT_BUTTON_DETAILS).shadow_root
        shadow_host2 = shadow_host1.find_element(*StartUnifiedProductPageLocators.SHADOW_ROOT2_BUTTON_DETAILS).shadow_root
        selector = shadow_host2.find_element(*StartUnifiedProductPageLocators.SHADOW_ROOT_OPTION).text
        assert selector == "ОПЦИЯ", "Диалоговое окно Опция не открылось"
