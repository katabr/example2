import time
import pytest
from selenium import webdriver
from .common_data.timeouts import Timeouts

# Stand = dev
stand = "dev"
local = "http://localhost:8081/"


@pytest.fixture # (scope="session")
def browser():
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    browser.implicitly_wait(Timeouts.TIMEOUT_10)
    #browser.maximize_window()
    yield browser
    browser.close()
    browser.quit()


@pytest.fixture
# @pytest.mark.parametrize(" product_id, channel_id", [("d4f03d9f-f00b-4713-99e9-df0ef60f5257", '7d6c39df-172f-4e6f-b2c1-29312e3adac7'),
#                                                      ("d4f03d9f-f00b-4713-99e9-df0ef60f5257", '17a90813-ac04-4a02-9800-ba449731207f'),
#                                                      ("d4f03d9f-f00b-4713-99e9-df0ef60f5257", '74acdcdd-c50a-4ceb-bd39-ace02cf97e22'),
#                                                      ("d4f03d9f-f00b-4713-99e9-df0ef60f5257", '1ef98ed1-a78f-467c-80c6-133d40bf91e6'),
#                                                      ("6043f523-9556-456b-b949-68fda9be9dcf", '130b6ca1-41fb-469f-b8f9-8ee79d946d73'),
#                                                      ("6043f523-9556-456b-b949-68fda9be9dcf", 'b77f0628-16a7-4ddc-aa65-2aa4b56bd1b4')])
def start_unified_sale(browser): #, product_id, channel_id):

    url = f"https://product-sale-stage.eland.corp.ru/?productSpecificationId=d4f03d9f-f00b&salesChannelId=7d6c39df"
    browser.get(url)


@pytest.fixture
def start_unified_sale_product(browser):

    url = f"https://product-sale-stage.eland.corp.ru/?productSpecificationId=f84b2e6f-25f3-456c-9745-ff58ed30cf21" \
          f"&salesChannelId=a4ed47bd-440d-4ef8-a2c1-acde2ff1753c"
    browser.get(url)


@pytest.fixture
def start_unified_sale_tarif(browser):

    url = f"https://product-sale-stage.eland.corp.ru/?productSpecificationId=d4f03d9f-f00b" \
          f"&salesChannelId=7d6c39df-172f"
    browser.get(url)


def pytest_addoption(parser):
    parser.addoption("--jira_issue", action="store")
    parser.addoption("--product_id", action="store")
    parser.addoption("--channel_id", action="store")


@pytest.fixture()
def console_params(pytestconfig):
    console_params = {"jira_issue": pytestconfig.getoption("--jira_issue"),
                      "product_id": pytestconfig.getoption("--product_id"),
                      "channel_id": pytestconfig.getoption("--channel_id"),}
    return console_params


@pytest.fixture(scope="class")
def localhost(browser):
    url = f"{local}"
    browser.get(url)


@pytest.fixture(scope="function")
def refresh(browser):
    yield browser
    browser.refresh()
