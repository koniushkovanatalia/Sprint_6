import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @allure.step('Закрыть плашку с куки, если она есть')
    def dismiss_cookies(self):
        try:
            button = self.find_element(MainPageLocators.cookie_button, timeout=10)
            button.click()
        except Exception:
            pass  # плашки нет — продолжаем

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.scroll_to(element)

    @allure.step('Ожидание прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        return self.wait_for_element_visible(locator)

    @allure.step('Кликнуть на панель с вопросом')
    def click_accordion_panel(self, index):
        locator_with_index = (MainPageLocators.accordion_heading[0],
                              MainPageLocators.accordion_heading[1].format(index))
        element = self.find_element(locator_with_index, timeout=20)
        self.scroll_to(element)
        try:
            element.click()
        except Exception:
            self.js_click(element)

    @allure.step('Проверить текст вопроса')
    def check_accordion_panel(self, index):
        locator_with_index = (MainPageLocators.accordion_panel[0],
                              MainPageLocators.accordion_panel[1].format(index))
        self.wait_for_non_empty_text(locator_with_index, timeout=15)
        return self.find_element(locator_with_index).text.strip()
















