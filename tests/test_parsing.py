import pytest
from classes.boards import Board
from tests.base_test import BaseTest
from pages.yug_auto_expert_page import YugAutoExpertPage
from parsers.yug_auto_expert_parser import YugAutoExpertParser
from services.telegram_service import public_ad_in_telegram
from classes.car import HyundaiTucson, HyundaiSantaFe, KiaSorento, KiaSportage


@pytest.mark.parametrize('car', [HyundaiTucson(), HyundaiSantaFe(), KiaSorento(), KiaSportage()])
class TestParsers(BaseTest):
    def test_parser_yug_auto_expert_tucson(self, car):
        self.visit_to(Board(car).get_yug_auto_expert_url())
        yug_auto_expert_page = YugAutoExpertPage(self.driver, car)
        yug_auto_expert_page.close_widgets()
        is_cars_present = yug_auto_expert_page.set_filters()
        if is_cars_present:
            page = yug_auto_expert_page.page_source()
            parsing_result = YugAutoExpertParser(page).parse()
            public_ad_in_telegram(parsing_result)
