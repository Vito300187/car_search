import pytest
from utils.factory_browser import get_driver
# from classes.car import HyundaiTucson, HyundaiSantaFe, KiaSorento, KiaSportage


@pytest.fixture
def driver(request):
    request.instance.driver = get_driver()
    yield
    request.instance.driver.close()
