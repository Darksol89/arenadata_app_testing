import pytest
import allure
from resources.pages.MainPage import MainPage
from resources.locators.Locators import MainLocators
from resources.common.parser_yaml import get_button_text

@allure.title('Check availability and text button')
@pytest.mark.parametrize('template_file, btn_param', [('google_template.yml', 'label')])
def test_check_button(browser_driver, get_url, get_template_directory, template_file, btn_param):
    btn_text = browser_driver.find_element(*MainLocators.JUST_BUTTON).text
    assert get_button_text(template_file, btn_param) == btn_text
    assert MainPage(browser_driver).click_test_button()


