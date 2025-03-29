import allure
import random

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class AddCustomerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
        self.add_customer_btn_main = (By.XPATH, '//button[@ng-class="btnClass1"]')
        self.post_code_field = (By.XPATH, '//input[@ng-model="postCd"]')
        self.first_name_field = (By.XPATH, '//input[@ng-model="fName"]')
        self.add_customer_btn = (By.XPATH, '//button[@class="btn btn-default"]')

    @allure.step(r"Нажать на кнопку add customer")
    def click_add_customer_btn(self):
        self.click_element(self.add_customer_btn_main)

    @allure.step(r"Сгенерировать Post Code")
    def generate_post_code(self) -> str:
        return ''.join([str(random.randint(0, 9)) for _ in range(10)])

    @allure.step(r"Вписать сгенерированный Post code в поле post code")
    def fill_field_post_code(self):
        self.fill_field(self.post_code_field ,self.generate_post_code())

    @allure.step(r"Сгенерировать имя на основе post code")
    def generate_first_name(self):
        chunks = [self.generate_post_code()[i:i+2] for i in range(0, len(self.generate_post_code()), 2)]
        first_name = ''
        with allure.step(r"Поиск букв по алфавиту"):
            for chunk in chunks:
                num = int(chunk)
                letter_index = num % 26
                letter = chr(letter_index + ord('a'))
                first_name += letter

        return first_name

    @allure.step(r"Вписать сгенерированное имя в поле для имени")
    def fill_field_first_name(self):
        self.fill_field(self.first_name_field, self.generate_first_name())

    @allure.step(r"Нажать на кнопку 'добавить клиента'")
    def click_add_customer_btn2(self):
        self.click_element(self.add_customer_btn)