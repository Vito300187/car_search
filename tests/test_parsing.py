from classes.boards import Board
from tests.base_test import BaseTest
from pages.yug_auto_expert_page import YugAutoExpertPage
from parsers.yug_auto_expert_parser import YugAutoExpertParser


class TestParsers(BaseTest):
    def test_parser_yug_auto_expert(self, cars_list):
        for car in cars_list:
            self.visit_to(Board(car).get_yug_auto_expert_url())
            yug_auto_expert_page = YugAutoExpertPage(self.driver, car)
            yug_auto_expert_page.close_widget()
            yug_auto_expert_page.set_filters()
            page = yug_auto_expert_page.page_source()
            YugAutoExpertParser(page).parse()
