from resources.locators.Locators import MainLocators
from resources.pages.BasePage import BasePage


class MainPage(BasePage):

    def click_test_button(self):
        self._click_to_element(MainLocators.JUST_BUTTON)
        return self

