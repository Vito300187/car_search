from pages.base_page import BasePage
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class YugAutoExpertPage(BasePage):
    automation_transmission_locator = (
        By.XPATH,
        '//li[@class="multiselect__element"]//span[contains(text(), "Автомат")]'
    )
    yapps_widget_close_xpath = "//div[contains(@id, 'YAppWidgets')]//div[contains(@class, 'YApps_Widget--Close')]"
    open_preferences_button_xpath = "//span[contains(text(), 'Все параметры')]"
    top_menu_city_xpath = "//span[@role='top-menu-city']"
    top_menu_city_list_xpath = "//div[contains(@class, 'top-menu-city-list')]"
    jivo_close_button_xpath = '//jdiv[contains(@id, "jivo_close_button")]/jdiv'
    transmission_placeholder_locator = (
        By.XPATH,
        '//span[contains(@class, "multiselect__placeholder") and contains(text(), "КПП")]'
    )

    def __init__(self, driver, car):
        super(YugAutoExpertPage, self).__init__(driver)
        self.car = car
        self.wait_time(3)

    def _choose_city(self, city='Краснодар'):
        self.driver.find_element(By.XPATH, self.top_menu_city_xpath).click()
        self.driver.find_element(By.XPATH, f"{self.top_menu_city_list_xpath}//a[@data-city='{city}']").click()
        self.wait_time(3)

    def _choose_brand(self):
        self.driver.find_element(
            By.XPATH,
            f'//div[contains(@class, "filter__list-item__name") and contains(text(), "{self.car.brand.capitalize()}")]'
        ).click()
        self.wait_for_element_visibility(
            (By.XPATH, f'//div[@class="list-tags"]/span[contains(text(), "{self.car.brand.capitalize()}")]'),
            timeout=5
        )

    def _choose_model(self):
        list_item_name = (By.XPATH, f'//div[contains(@class, "filter__list-item__name") and contains(text(), "{self.car.model.title()}")]')
        list_tags = (By.XPATH, f'//div[@class="list-tags"]//span[contains(text(), "{self.car.model.title()}")]')
        if self.is_element_displayed(list_item_name, timeout=3):
            self.driver.find_element(*list_item_name).click()
            self.wait_for_element_visibility(list_tags, timeout=5)
        else:
            raise Exception('Models are not present on the page')

    def _choose_transmission(self):
        self.driver.find_element(*self.transmission_placeholder_locator).click()
        self.driver.find_element(*self.automation_transmission_locator).click()

    def _enter_text_in_field(self, field_xpath, value):
        field = self.driver.find_element(By.XPATH, field_xpath)
        field.clear()
        field.send_keys(value)
        field.send_keys(Keys.ENTER)

    def _open_preferences(self):
        self.driver.find_element(By.XPATH, self.open_preferences_button_xpath).click()

    def _close_widgets_list(self):
        waiting_timeout_banner_and_jdiv = 20
        self.wait_time(waiting_timeout_banner_and_jdiv)
        close_widgets_list = self.driver.find_elements(By.XPATH, self.yapps_widget_close_xpath)
        close_widgets = list(filter(lambda x: x.is_displayed(), close_widgets_list))
        if any(close_widgets):
            close_widgets[0].click()
            print('Widget was closed')

    def _close_jivo_player(self):
        if self.is_element_displayed((By.XPATH, self.jivo_close_button_xpath)):
            self.driver.find_element(By.XPATH, self.jivo_close_button_xpath).click()
            print('Jivo player was closed')

    def close_widgets(self):
        self._close_widgets_list()
        self._close_jivo_player()

    def set_filters(self):
        self._choose_city()
        self._choose_brand()
        self._choose_model()
        self._open_preferences()
        self._choose_transmission()

    def page_source(self):
        return self.driver.page_source
