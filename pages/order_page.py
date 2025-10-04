import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderLocators

class OrderPage(BasePage):

    @allure.step('Клик по кнопке "Заказать" вверху страницы')
    def click_order_header_button(self):
        self.click(OrderLocators.order_button_header)

    @allure.step('Клик по кнопке "Заказать" в центре страницы')
    def click_order_centre_button(self):
        element = self.find_element(OrderLocators.order_button_centre)
        self.scroll_to(element)
        self.click(OrderLocators.order_button_centre)

    @allure.step('Ввести имя: {name}')
    def set_first_name(self, name):
        element = self.find_element(OrderLocators.first_name_input)
        element.send_keys(name)

    @allure.step('Ввести фамилию: {surname}')
    def set_last_name(self, surname):
        element = self.find_element(OrderLocators.last_name_input)
        element.send_keys(surname)

    @allure.step('Ввести адрес: {address}')
    def set_address(self, address):
        element = self.find_element(OrderLocators.address_input)
        element.send_keys(address)

    @allure.step('Выбрать станцию метро: {metro}')
    def set_metro(self, metro):
        metro_input = self.find_element(OrderLocators.metro_input)
        metro_input.send_keys(metro)
        metro_option = (OrderLocators.metro_option[0], OrderLocators.metro_option[1].format(metro))
        self.click(metro_option)

    @allure.step('Ввести телефон: {phone}')
    def set_phone(self, phone):
        element = self.find_element(OrderLocators.phone_input)
        element.send_keys(phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.click(OrderLocators.next_button)

    @allure.step('Установить дату доставки: {date}')
    def set_date(self, date):
        self.click(OrderLocators.date_input)
        day_locator = (OrderLocators.date_day[0], OrderLocators.date_day[1].format(date))
        self.click(day_locator)

    @allure.step('Выбрать срок аренды: {days}')
    def set_rental_period(self, days):
        self.click(OrderLocators.rental_period_dropdown)
        option_locator = (OrderLocators.rental_period_option[0], OrderLocators.rental_period_option[1].format(days))
        self.click(option_locator)

    @allure.step('Выбрать цвет(а) самоката: {colours}')
    def set_colour(self, colours):
        if isinstance(colours, str):
            colours = [colours]
        for colour in colours:
            if colour.lower() == "black":
                self.click(OrderLocators.colour_black)
            elif colour.lower() == "grey":
                self.click(OrderLocators.colour_grey)

    @allure.step('Установить комментарий курьеру: {comment}')
    def set_comment(self, comment):
        element = self.find_element(OrderLocators.comment_field)
        element.send_keys(comment)

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
        self.click(OrderLocators.order_button)

    @allure.step('Проверить, что появилось модальное окно "Хотите оформить заказ?"')
    def wait_for_order_modal(self):
        self.wait_for_element_visible(OrderLocators.order_modal_header)

    @allure.step('Подтвердить заказ, нажав кнопку "Да"')
    def confirm_order(self):
        self.click(OrderLocators.confirm_order_button)

    @allure.step('Проверить, что появилось модальное окно "Заказ оформлен"')
    def get_order_confirmation_text(self):
        element = self.wait_for_element_visible(OrderLocators.order_confirmation_modal, timeout=10)
        return element.text.strip()







