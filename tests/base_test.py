import pytest


@pytest.mark.usefixtures("driver")
class BaseTest:
    def visit_to(self, url):
        self.driver.get(url)
