import allure
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderLocators

class OrderPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    @allure.step('Кликнуть на кнопку "Заказать"')
    def click_to_order_button(self, locator):
        order_button = self.wait.until(EC.element_to_be_clickable(locator))
        order_button.click()

    @allure.step('Ввести имя: {name}')
    def set_first_name(self, name):
        element = self.wait.until(EC.visibility_of_element_located(OrderLocators.first_name_input))
        element.send_keys(name)

    @allure.step('Ввести фамилию: {surname}')
    def set_last_name(self, surname):
        element = self.wait.until(EC.visibility_of_element_located(OrderLocators.last_name_input))
        element.send_keys(surname)

    @allure.step('Ввести адрес: {address}')
    def set_address(self, address):
        element = self.wait.until(EC.visibility_of_element_located(OrderLocators.address_input))
        element.send_keys(address)

    @allure.step('Выбрать станцию метро: {metro}')
    def set_metro(self, metro):
        metro_input = self.wait.until(EC.visibility_of_element_located(OrderLocators.metro_input))
        metro_input.send_keys(metro)
        metro_option = (OrderLocators.metro_option[0], OrderLocators.metro_option[1].format(metro))
        self.wait.until(EC.element_to_be_clickable(metro_option)).click()

    @allure.step('Ввести телефон: {phone}')
    def set_phone(self, phone):
        element = self.wait.until(EC.visibility_of_element_located(OrderLocators.phone_input))
        element.send_keys(phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.wait.until(EC.element_to_be_clickable(OrderLocators.next_button)).click()

    @allure.step('Установить дату доставки: {date}')
    def set_date(self, date):
        # клик по полю даты
        element = self.wait.until(EC.element_to_be_clickable(OrderLocators.date_input))
        element.click()

        # выбор дня
        day_locator = (OrderLocators.date_day[0], OrderLocators.date_day[1].format(date))
        day_element = self.wait.until(EC.element_to_be_clickable(day_locator))
        day_element.click()

    @allure.step('Выбрать срок аренды: {days}')
    def set_rental_period(self, days):
        self.wait.until(EC.element_to_be_clickable(OrderLocators.rental_period_dropdown)).click()
        option_locator = (OrderLocators.rental_period_option[0], OrderLocators.rental_period_option[1].format(days))
        self.wait.until(EC.element_to_be_clickable(option_locator)).click()

    @allure.step('Выбрать цвет(а) самоката: {colours}')
    def set_colour(self, colours):
        if isinstance(colours, str):
            colours = [colours]
        for colour in colours:
            if colour.lower() == "black":
                self.wait.until(EC.element_to_be_clickable(OrderLocators.colour_black)).click()
            elif colour.lower() == "grey":
                self.wait.until(EC.element_to_be_clickable(OrderLocators.colour_grey)).click()

    @allure.step('Установить комментарий курьеру: {comment}')
    def set_comment(self, comment):
        element = self.wait.until(EC.visibility_of_element_located(OrderLocators.comment_field))
        element.send_keys(comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.wait.until(EC.element_to_be_clickable(OrderLocators.order_button)).click()

    @allure.step('Проверить, что появилось модальное окно "Хотите оформить заказ?"')
    def wait_for_order_modal(self):
        self.wait.until(EC.visibility_of_element_located(OrderLocators.order_modal_header))

    @allure.step('Подтвердить заказ, нажав кнопку "Да"')
    def confirm_order(self):
        self.wait.until(EC.element_to_be_clickable(OrderLocators.confirm_order_button)).click()

    @allure.step('Проверить, что появилось модальное окно "Заказ оформлен"')
    def wait_for_order_confirmation(self):
        self.wait.until(EC.visibility_of_element_located(OrderLocators.order_confirmation_modal))





















