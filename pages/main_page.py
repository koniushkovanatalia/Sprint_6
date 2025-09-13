import allure
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from locators.main_page_locators import MainPageLocators


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Закрыть плашку с куки, если она есть')
    def dismiss_cookies(self):
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(MainPageLocators.cookie_button)
            )
            button.click()
        except TimeoutException:
            pass  # плашки нет — продолжаем

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Ожидание прогрузки элемента')
    def wait_visibility_of_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Кликнуть на панель с вопросом')
    def click_accordion_panel(self, index):
        locator_with_index = (By.ID, MainPageLocators.accordion_heading[1].format(index))
        element = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(locator_with_index)
        )
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Проверить текст вопроса')
    def check_accordion_panel(self, index):
        locator_with_index = (By.ID, MainPageLocators.accordion_panel[1].format(index))
        # ждём, пока текст не появится
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(locator_with_index, "")  # пустая строка, ждём появления любого текста
        )
        accordion_panel_text = self.driver.find_element(*locator_with_index).text.strip()
        return accordion_panel_text
















