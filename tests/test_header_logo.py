import allure
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.header_locators import HeaderLocators
from data import TestData
from pages.header_page import HeaderPage

class TestHeaderLogo:
    @allure.title('Проверка перехода на главную страницу Самоката по клику на логотип "Самокат"')
    def test_scooter_logo_redirect(self, driver):
        driver.get(TestData.ORDER_PAGE_URL)

        header = HeaderPage(driver)
        header.click_scooter_logo()
        header.wait_for_url(TestData.BASE_URL)

        assert driver.current_url == TestData.BASE_URL

    @allure.title('Проверка открытия в новом окне через редирект главной страницы Дзена по клику на логотип "Яндекс"')
    def test_yandex_logo_redirect(self, driver):

        header = HeaderPage(driver)
        header.click_yandex_logo()

        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])

        header.wait_for_url('https://dzen.ru/?yredirect=true')

        assert driver.current_url == 'https://dzen.ru/?yredirect=true'






