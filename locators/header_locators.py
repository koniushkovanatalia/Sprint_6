import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

class HeaderLocators:
    scooter_logo = (By.XPATH, '//img[@alt="Scooter"]') # логотип "Яндекс"
    yandex_logo = (By.XPATH, '//img[@alt="Yandex"]') # логотип "Самокат"