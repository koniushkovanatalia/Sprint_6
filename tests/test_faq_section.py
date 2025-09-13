import allure
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException


from locators.main_page_locators import MainPageLocators
from data import TestData
from pages.main_page import MainPage

class TestMainPage:
    @allure.title('Проверка FAQ: текст ответа на вопрос совпадает с ожидаемым')
    @pytest.mark.parametrize('index, expected_text', TestData.test_data_question_answer)
    def test_faq_question_displays_correct_answer(self, driver, index, expected_text):
        faq_section = MainPage(driver)
        faq_section.dismiss_cookies()
        heading_locator = (By.ID, MainPageLocators.accordion_heading[1].format(index))
        faq_section.scroll_to_element(heading_locator)
        faq_section.wait_visibility_of_element(heading_locator)
        faq_section.click_accordion_panel(index)
        result = faq_section.check_accordion_panel(index)
        assert result == expected_text












