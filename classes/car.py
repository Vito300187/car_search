class Car:
    def __init__(self):
        self.condition = 'used'
        self.s_probegom = 's_probegom'
        self.maxprice = 2700000
        self.minyear = 2017
        self.maxyear = 2021
        self.maxprobeg = 80000
        self.city = 'Краснодар'


class HyundaiSantaFe(Car):
    def __init__(self):
        super().__init__()
        self.brand = 'hyundai'
        self.model_snake_case_name = 'santa_fe'
        self.model = 'Santa Fe'


class HyundaiTucson(Car):
    def __init__(self):
        super().__init__()
        self.brand = 'hyundai'
        self.model = 'tucson'


class KiaSportage(Car):
    def __init__(self):
        super().__init__()
        self.brand = 'kia'
        self.model = 'sportage'


class KiaSorento(Car):
    def __init__(self):
        super().__init__()
        self.brand = 'kia'
        self.model = 'sorento'
