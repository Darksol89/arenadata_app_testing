import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    """Parser for command-line parameters"""
    parser.addoption('--url',
                     action='store',
                     default='http://localhost:5000',
                     help='Target link for request')

class BaseSetUp:

    @pytest.fixture()
    def browser_driver(self):
        """Initializing webdriver and start web browser"""
        print('Start Chrome browser...\n')
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

        yield browser
        print('Close Chrome browser...\n')
        browser.quit()

    @pytest.fixture()
    def get_url(self, request, browser_driver):
        """Open url for testing"""
        url = request.config.getoption('--url')
        open_link = browser_driver.get(url)
        browser_driver.implicitly_wait(7)

        return open_link