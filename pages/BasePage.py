from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = int(timeout)
        self.wait = WebDriverWait(driver, timeout)
        self.page_url = ''

    def find_element(self, by: By or int, value: str) -> WebElement:
        return self.wait.until(expected_conditions.visibility_of_element_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    def find_elements(self, by: By or int, value: str) -> list[WebElement]:
        return self.wait.until(expected_conditions.visibility_of_all_elements_located((by, value)),
                               message=f'Элемент {by, value} не найден')

    def get_element(self, locator) -> WebElement:
        element = self.find_element(*locator)
        return element

    def click_element(self, locator) -> None:
        element = self.find_element(*locator)
        element.click()

    def get_text(self, locator) -> str:
        element = self.find_element(*locator)
        return element.text

    def fill_field(self, locator, value):
        """
        Заполняет поле.
        :param locator: Локатор
        :param value: Значение, которое нужно вписать
        :return:
        """
        field = self.find_element(*locator)
        field.clear()  # очищаем поле перед вводом
        field.send_keys(value)

    def get_element_displayed(self, locator):
        return self.find_element(*locator).is_displayed()

    def driver_url(self, page_url) -> str:
        return self.driver.get(page_url)