import allure

from pages.base_page import BasePage
from locators.header_locators import HeaderLocators

class HeaderPage(BasePage):

    @allure.step('Клик на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.click(HeaderLocators.yandex_logo)

    @allure.step('Клик на логотип "Самокат"')
    def click_scooter_logo(self):
        self.click(HeaderLocators.scooter_logo)

    @allure.step('Дождаться загрузки страницы по URL')
    def wait_for_url(self, expected_url):
        return super().wait_for_url(expected_url)

    @allure.step('Переключиться на новое окно')
    def switch_to_new_window(self):
        return super().wait_for_new_window_and_switch()

    @allure.step('Получить текущий URL')
    def get_current_url(self):
        return super().get_current_url()






