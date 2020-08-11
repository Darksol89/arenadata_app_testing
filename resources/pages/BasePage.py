from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, driver):
        """Initialize web driver"""
        self.driver: WebDriver = driver


    def _click_to_element(self, locator):
        """Click to web element"""
        try:
            self.driver.implicitly_wait(3)
            WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(locator))
        except NoSuchElementException:
            print('Element is not found')
        finally:
            self.driver.find_element(*locator).click()
