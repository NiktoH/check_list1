import allure

from selenium.webdriver.common.by import By
from pages.BasePage import BasePage


class CustomerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, timeout=60)

        self.page_url = 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'
        self.customers_btn = (By.XPATH, '//button[@ng-class="btnClass3"]')
        self.first_name_href = (By.XPATH, '//td[1]//a')
        self.table = (By.XPATH, '//table/tbody/tr')
        self.table_row = (By.XPATH, '//table/tbody/tr//td[1]')
        self.search_customer_field = (By.XPATH, '//input[@ng-model="searchCustomer"]')
        self.delete_btn = (By.XPATH, '//button[@ng-click="deleteCust(cust)"]')


    @allure.step(r"Нажать на кнопку Customers")
    def click_customers_btn(self):
        self.click_element(self.customers_btn)

    @allure.step(r"Нажать на first name для сортировки")
    def click_first_name_href(self):
        self.click_element(self.first_name_href)

    @allure.step(r"Найти и удалить клиента по ср. арифметической")
    def find_and_delete_customer(self):
        table_rows = self.find_elements(*self.table)
        names = [row.find_element(*self.table_row).text for row in table_rows]
        lengths = [len(name) for name in names]
        average_length = sum(lengths) / len(lengths)
        closest_name = min(names, key=lambda name: abs(len(name) - average_length))
        with allure.step(r"Заполнить поле найденным именем"):
            self.fill_field(self.search_customer_field, closest_name)
        with allure.step(r"Кликнуть по кнопке delete"):
            self.click_element(self.delete_btn)