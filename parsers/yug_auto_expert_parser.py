from parsel import Selector
import hashlib


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

    @staticmethod
    def _model_card_hash(params):
        return hashlib.sha256(
            ''.join(params.values()).encode()
        ).hexdigest()

    def _parse_helper(self, card):
        return {
            'image': card.xpath(self.model_image_card).attrib['src'],
            'link': f"https://yug-avto-expert.ru{card.xpath(self.model_link_card).attrib['href']}",
            'power': card.xpath(f'{self.model_power_card}/text()')[4].get(),
            'price': card.xpath(f'{self.model_price_card}/text()').get(),
            'distance': card.xpath(f'{self.model_distance_card}/text()')[1].get(),
            'year': card.xpath(f'{self.model_year_card}/text()')[0].get()
        }

    def parse(self):
        selector = Selector(text=self.page_source)
        model_cards = selector.xpath(self.model_cards)
        result_pars_cars = []
        for card in model_cards:
            params = self._parse_helper(card)
            params['hash'] = self._model_card_hash(params)
            result_pars_cars.append(params)

        return result_pars_cars
