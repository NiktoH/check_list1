import allure

from pages.AddCustomerPage import AddCustomerPage
from pages.BasePage import BasePage
from pages.CustomerPage import CustomerPage


@allure.title(r"Добавление клиента в базу")
def test_1_add_customer(driver):
    base = BasePage(driver)
    base.driver_url('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager')

    add_customer_page = AddCustomerPage(driver)
    add_customer_page.click_add_customer_btn()
    assert len(add_customer_page.generate_post_code()) == 10 , "Код больше или меньше 10 символов"
    add_customer_page.fill_field_post_code()
    add_customer_page.generate_first_name()
    add_customer_page.fill_field_first_name()
    add_customer_page.click_add_customer_btn2()

@allure.title(r"Сортировка клиента")
def test_2_sort_customers(driver):
    base = BasePage(driver)
    base.driver_url('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager')

    customer_page = CustomerPage(driver)
    customer_page.click_customers_btn()
    customer_page.click_first_name_href()

@allure.title(r"Удаление клиента из базы")
def test_3_delete_customers(driver):
    base = BasePage(driver)
    base.driver_url('https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager')

    customer_page = CustomerPage(driver)
    customer_page.click_customers_btn()
    customer_page.find_and_delete_customer()