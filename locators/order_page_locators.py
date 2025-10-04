import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

class OrderLocators:
    # кнопка "Заказать"
    order_button_header = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and not(contains(@class, 'Button_Middle__1CSJM'))]")  # кнопка "Заказать" вверху страницы
    order_button_centre = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM')]")  # кнопка "Заказать" под блоком "Как это работает"

    # окно "Для кого самокат"
    first_name_input = (By.XPATH, "//input[@placeholder='* Имя']") # поле "Имя"
    last_name_input = (By.XPATH, "//input[@placeholder='* Фамилия']") # поле "Фамилия"
    address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']") # поле "Адрес"
    metro_input = (By.XPATH, "//input[@placeholder='* Станция метро']") # поле "Станция метро"
    metro_option = (By.XPATH, "//div[@class='select-search__select']//div[text()='{}']") # выпадающий список со станциями
    phone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']") # поле "Телефон"
    next_button = (By.XPATH, "//button[text()='Далее']") # кнопка "Далее"

    # окно "Про аренду"
    date_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # поле "Дата"
    date_day = (By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='{}']") # календарь
    rental_period_dropdown = (By.XPATH, "//div[@class='Dropdown-placeholder' and text()='* Срок аренды']") # поле "Срок аренды"
    rental_period_option = (By.XPATH, "//div[@class='Dropdown-option' and text()='{}']") # выпадающий список с количеством дней аренды
    colour_black = (By.XPATH, '//label[@for="black"]') # цвет самоката "чёрный жемчуг"
    colour_grey = (By.XPATH, '//label[@for="grey"]') # цвет самоката "серая безысходность"
    comment_field = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]') # поле "Комментарий для курьера"
    order_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']") # кнопка "Заказать"
    back_button = (By.XPATH, "//button[contains(@class, 'Button_Inverted__3IF-i') and text()='Назад']") # кнопка "Назад"

    # окно "Хотите оформить заказ?"
    order_modal_header = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Хотите оформить заказ?')]") # заголовок "Хотите оформить заказ?"
    confirm_order_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Да']") # кнопка "Да"
    cancel_order_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Нет']") # кнопка "Нет"

    # окно "Заказ оформлен"
    order_confirmation_modal = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader__3FDaJ') and contains(text(), 'Заказ оформлен')]") # подтверждение заказа
    view_order_status_button = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Посмотреть статус']") # кнопка "Посмотреть статус"













