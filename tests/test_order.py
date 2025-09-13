import allure
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from locators.order_page_locators import OrderLocators
from data import TestData
from pages.order_page import OrderPage

class TestOrderScooter:
    @allure.title('Заказ самоката через кнопку "Заказать" вверху страницы')
    @pytest.mark.parametrize("order_data", [TestData.order_data[0]])
    def test_order_scooter_from_header_button_success(self, driver, order_data):
        order_page = OrderPage(driver)

        order_page.click_to_order_button(OrderLocators.order_button_header)
        order_page.set_first_name(order_data["name"])
        order_page.set_last_name(order_data["surname"])
        order_page.set_address(order_data["address"])
        order_page.set_metro(order_data["metro_station"])
        order_page.set_phone(order_data["phone"])
        order_page.click_next_button()
        order_page.set_date(order_data["date"])
        order_page.set_rental_period(order_data["rental_period"])
        order_page.set_colour(order_data["colour"])
        order_page.set_comment(order_data["comment"])
        order_page.click_order_button()
        order_page.wait_for_order_modal()
        order_page.confirm_order()
        confirmation_element = driver.find_element(*OrderLocators.order_confirmation_modal)
        assert "Заказ оформлен" in confirmation_element.text

    @allure.title('Заказ самоката через кнопку "Заказать" внизу страницы')
    @pytest.mark.parametrize("order_data", [TestData.order_data[1]])
    def test_order_scooter_from_centre_button_success(self, driver, order_data):
        order_page = OrderPage(driver)

        order_page.scroll_to_element(OrderLocators.order_button_centre)
        order_page.click_to_order_button(OrderLocators.order_button_centre)
        order_page.set_first_name(order_data["name"])
        order_page.set_last_name(order_data["surname"])
        order_page.set_address(order_data["address"])
        order_page.set_metro(order_data["metro_station"])
        order_page.set_phone(order_data["phone"])
        order_page.click_next_button()
        order_page.set_date(order_data["date"])
        order_page.set_rental_period(order_data["rental_period"])
        order_page.set_colour(order_data["colour"])
        order_page.set_comment(order_data["comment"])
        order_page.click_order_button()
        order_page.wait_for_order_modal()
        order_page.confirm_order()
        confirmation_element = driver.find_element(*OrderLocators.order_confirmation_modal)
        assert "Заказ оформлен" in confirmation_element.text





