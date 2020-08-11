import pytest
import allure
from resources.pages.MainPage import MainPage
from resources.locators.Locators import MainLocators

url = 'http://localhost:5000'


@allure.title('Check and click button in Main Page site')
@pytest.mark.parametrize('template_file', ['google_template.yml'])
def test_available_button_in_main_page(browser_driver, api_client,
                                       get_template_directory, template_file):
    api_client.upload_template(template_file=template_file)
    # Getting template name without format
    template_name = template_file.split(sep='.')
    api_client.install_template(template_name[0])
    # Opening url
    browser_driver.get(url)

    assert MainPage(browser_driver).click_test_button()


@allure.title('Check of unavailable button in Main Page site')
@pytest.mark.parametrize('template_file', ['yandex_template_no_link.yml'])
def test_unavailable_button_in_main_page(browser_driver, api_client,
                                         get_template_directory, template_file):
    api_client.upload_template(template_file=template_file)
    # Getting template name without format
    template_name = template_file.split(sep='.')
    api_client.install_template(template_name[0])
    # Opening url
    browser_driver.get(url)

    assert browser_driver.find_element(*MainLocators.BTN_NO_LINK)
    assert not browser_driver.find_element(*MainLocators.BTN_NO_LINK).click()
