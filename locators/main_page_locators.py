
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

class MainPageLocators:

    home_subheader = (By.CLASS_NAME, 'Home_SubHeader__zwi_E')  # Заголовок "Вопросы о важном"
    accordion_heading = (By.ID, 'accordion__heading-{}')  # Вопросы
    accordion_panel = (By.ID, 'accordion__panel-{}')  # Ответы
    cookie_banner = (By.CLASS_NAME, "App_CookieConsent__1yUIN")  # плашка "И здесь куки! В общем, мы их используем."
    cookie_button = (By.ID, "rcc-confirm-button")  # кнопка "да все привыкли"

