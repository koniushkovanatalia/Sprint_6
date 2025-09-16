import allure
import pytest

from data import TestData
from pages.header_page import HeaderPage

class TestHeaderLogo:

    @allure.title('Проверка перехода на главную страницу Самоката по клику на логотип "Самокат"')
    def test_scooter_logo_redirect(self, driver):
        driver.get(TestData.ORDER_PAGE_URL)

        header = HeaderPage(driver)
        header.click_scooter_logo()
        header.wait_for_url(TestData.BASE_URL)

        assert header.get_current_url() == TestData.BASE_URL

    @allure.title('Проверка открытия в новом окне через редирект главной страницы Дзена по клику на логотип "Яндекс"')
    def test_yandex_logo_redirect(self, driver):
        driver.get(TestData.ORDER_PAGE_URL)  # добавляем, чтобы тест был самодостаточным

        header = HeaderPage(driver)
        header.click_yandex_logo()
        header.switch_to_new_window()
        header.wait_for_url('https://dzen.ru/?yredirect=true')

        assert header.get_current_url() == 'https://dzen.ru/?yredirect=true'






