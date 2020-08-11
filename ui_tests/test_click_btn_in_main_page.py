import pytest
import allure
from resources.pages.MainPage import MainPage



@allure.title('Click button in Main Page site')
@pytest.mark.parametrize('template_file', ['yandex_template.yml'])
def test_click_button_in_main_page(api_client, get_template_directory,
                                   template_file):
    api_client.upload_template(template_file=template_file)
    template_name = template_file.split(sep='.')
    api_client.install_template(template_name[0])
    browser = browser_driver()
    open_url = get_url
    assert MainPage(browser).click_test_button()
