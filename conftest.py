import pytest
import allure
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from utils.api import Api


def pytest_addoption(parser):
    """Parser parameters for testing"""
    parser.addoption('--url',
                     action='store',
                     default='http://localhost:5000',
                     help='Target link for request')
    parser.addoption('--template_dir',
                     action='store',
                     default='D:\\PyCharm_projects\\Arenadata_task\\templates',
                     help='Directory with templates for tests')


@pytest.fixture()
def api_client(request):
    """Getting url for api tests"""
    base_url = request.config.getoption('--url')
    return Api(base_url)


@pytest.fixture()
@allure.step('Getting working directory with templates')
def get_template_directory(request):
    """Getting working directory with templates"""
    template_directory = request.config.getoption('--template_dir')
    os.chdir(template_directory)
    return template_directory


@pytest.fixture()
def browser_driver():
    """Initializing webdriver and start web browser"""
    print('Start Chrome browser...\n')
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    yield browser
    print('Close Chrome browser...\n')
    browser.quit()
