import time
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @staticmethod
    def wait_time(second):
        time.sleep(second)

    def is_element_displayed(self, element_locator, timeout=15):
        self.driver.implicitly_wait(2)
        try:
            element = WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(element_locator))
            return element.is_displayed()
        except TimeoutException:
            return False
        finally:
            self.driver.implicitly_wait(30)

    def wait_for_element_visibility(self, element_locator, timeout=15):
        self.driver.implicitly_wait(2)
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(element_locator))
        finally:
            self.driver.implicitly_wait(30)
