from parsel import Selector
from utils.helpers import get_model_card_hash, safety_wrapper


class YugAutoExpertParser:
    model_cards = '//div[@class="model__grid-card"]'
    model_image_card = './div[contains(@class, "model__grid-card__head")]/a/img'
    model_link_card = './div[contains(@class, "model__grid-card__head")]/a'
    model_power_card = './/span[@class="model__grid-card__content--list-item"]'
    model_price_card = './/div[@class="model__grid-card__content--price_curent"]'
    model_distance_card = './/span[@class="model__grid-card__content--list-item"]'
    model_year_card = './/span[@class="model__grid-card__content--list-item"]'

    def __init__(self, page_source):
        self.page_source = page_source

    def _parse_image(self, card):
        return safety_wrapper(card.xpath(self.model_image_card).attrib['src'])

    def _parse_link(self, card):
        return safety_wrapper(f"https://yug-avto-expert.ru{card.xpath(self.model_link_card).attrib['href']}")

    def _parse_power(self, card):
        try:
            card.xpath(f'{self.model_power_card}/text()')[4].get()
        except [IndexError, OSError, EOFError, EnvironmentError, ValueError]:
            return ''

    def _parse_price(self, card):
        return safety_wrapper(card.xpath(f'{self.model_price_card}/text()').get())

    def _parse_distance(self, card):
        return safety_wrapper(card.xpath(f'{self.model_distance_card}/text()')[1].get())

    def _parse_year(self, card):
        return safety_wrapper(card.xpath(f'{self.model_year_card}/text()')[0].get())

    def _parse_helper(self, card):
        return {
            'image': self._parse_image(card),
            'link': self._parse_link(card),
            'power': self._parse_power(card),
            'price': self._parse_price(card),
            'distance': self._parse_distance(card),
            'year': self._parse_year(card)
        }

    def parse(self):
        selector = Selector(text=self.page_source)
        model_cards = selector.xpath(self.model_cards)
        result_pars_cars = []
        for card in model_cards:
            params = self._parse_helper(card)
            params['hash'] = get_model_card_hash(params)
            result_pars_cars.append(params)
        return result_pars_cars
