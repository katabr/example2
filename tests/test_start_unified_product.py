# Тест-сьют проверяет функции стартовой страницы Универсального лендинга продажи монопродукта

import pytest
import allure

from ..pages.account_page import AccountPage
from ..pages.start_unified_product_page import StartUnifiedProductPage

# Чистый тестовый номер
number = '79118888888'
code = 'test'


@allure.feature("Универсальный лендинг продажи")
@allure.suite("Продажа Монопродукта")
class TestUnifiedSaleMonoProduct:

    # USMP-1
    @allure.testcase("Проверка авторизации Универсального лендинга продажи монопродукта")
    @allure.title("Авторизация с известным каналом и продуктом для монопродукта")
    @allure.description("Проверка авторизации с известным каналом и продуктом для монопродукта")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_authorization_unified_sale_with_chanel_and_product_for_product(self, browser, start_unified_sale_product):
        acp = AccountPage(browser)
        with allure.step("Ввести номер и код"):
            acp.authorization(number, code)
        with allure.step("Проверить, что осуществлен вход в аккаунт"):
            acp.should_be_photo_account()

    # USMP-2
    @allure.testcase("Проверка доступности оффера для Оформления заказа для монопродукта")
    @allure.title("Кликабельность кнопки Оформить заказ при оффере для монопродукта")
    @allure.description("Проверка кликабельности кнопки Оформить заказ при оффере для монопродукта")
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_check_clickable_button_order_for_product(self, browser, start_unified_sale_product):
        acp = AccountPage(browser)
        supp = StartUnifiedProductPage(browser)
        with allure.step("Ввести номер и код"):
            acp.authorization(number, code)
        with allure.step("Проверить, что осуществлен вход в аккаунт"):
            acp.should_be_photo_account()
        with allure.step("Проверить возможность подключения"):
            supp.should_be_clickable_plugging_button()
