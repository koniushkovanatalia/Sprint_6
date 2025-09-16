import allure
import pytest

from data import TestData
from pages.main_page import MainPage

class TestMainPage:
    @allure.title('Проверка FAQ: текст ответа на вопрос совпадает с ожидаемым')
    @pytest.mark.parametrize('index, expected_text', TestData.test_data_question_answer)
    def test_faq_question_displays_correct_answer(self, driver, index, expected_text):
        faq_section = MainPage(driver)
        faq_section.dismiss_cookies()
        faq_section.click_accordion_panel(index)
        result = faq_section.check_accordion_panel(index)
        assert result == expected_text













