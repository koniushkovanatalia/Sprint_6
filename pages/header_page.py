import allure
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.header_locators import HeaderLocators


class HeaderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Клик на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.driver.find_element(*HeaderLocators.yandex_logo).click()

    @allure.step('Клик на логотип "Самокат"')
    def click_scooter_logo(self):
        self.driver.find_element(*HeaderLocators.scooter_logo).click()

    @allure.step('Дождаться загрузки страницы по заголовку или URL')
    def wait_for_url(self, expected_url):
        return WebDriverWait(self.driver, 10).until(
            EC.url_to_be(expected_url)
        )





