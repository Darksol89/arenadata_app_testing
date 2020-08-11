"""Locators for web elements"""
from selenium.webdriver.common.by import By


class MainLocators:
    BTN_LINK = (By.CSS_SELECTOR, 'a[role="button"]')
    BTN_NO_LINK = (By.CSS_SELECTOR, 'button.disabled')
