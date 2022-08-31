from parsel import Selector
from utils.helpers import get_model_card_hash


class YugAutoExpertParser:
    model_grid_card = '//div[@class="model__grid-card__content--list"]'
    model_cards = '//div[@class="model__grid-card"]'
    model_link_card = './/div[contains(@class, "model__grid-card__head")]/a'
    model_image_card = f'{model_link_card}/img'
    model_price_card = './/div[@class="model__grid-card__content--price_curent"]'

    def __init__(self, page_source):
        self.page_source = page_source

    def _parse_image(self, card):
        return card.xpath(self.model_image_card).attrib['src']

    def _parse_link(self, card):
        return f"https://yug-avto-expert.ru{card.xpath(self.model_link_card).attrib['href']}"

    def _parse_fuel(self, card):
        return card.xpath(f'{self.model_grid_card}')[1].xpath('.//span/text()')[0].get()

    def _parse_price(self, card):
        return card.xpath(f'{self.model_price_card}/text()').get()

    def _parse_year(self, card):
        return card.xpath(f'{self.model_grid_card}')[0].xpath('.//span/text()')[0].get()

    def _parse_distance(self, card):
        return card.xpath(f'{self.model_grid_card}')[0].xpath('.//span/text()')[1].get()

    def _parse_helper(self, card):
        return {
            'image': self._parse_image(card),
            'link': self._parse_link(card),
            'power': self._parse_fuel(card),
            'price': self._parse_price(card),
            'distance': self._parse_distance(card),
            'year': self._parse_year(card)
        }

    def parse(self):
        selector = Selector(text=self.page_source)
        model_cards = selector.xpath(self.model_cards)
        result_pars_cars = []
        for card in model_cards:
            if 'Продать автомобиль' or 'Рассчитайте ежемесячный платеж' in card.xpath('./div').extract()[0]:
                continue
            params = self._parse_helper(card)
            params['hash'] = get_model_card_hash(params)
            result_pars_cars.append(params)
        return result_pars_cars
