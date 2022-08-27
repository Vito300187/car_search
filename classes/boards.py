class Board:
    def __init__(self, car):
        self.car = car

    def get_avito_url(self):
        return "https://www.avito.ru/krasnodar/avtomobili/"\
               f"{self.car.condition}/"\
               f"{self.car.brand}/"\
               f"{self.car.model}-"\
               "ASgBAgICA0SGFMjmAeC2DaKbMeK2Dd6bMQ?f=" \
               "ASgBAQECBETyCrCKAYYUyOYB4LYNopsx4rYN3psx" \
               "AkDwChSsigHwtg008Lco8rco7rco" \
               "A0X4Ahp7ImZyb20iOjE5Nzc1LCJ0byI6NTA1NTQ3fb4VGHsiZnJvbSI6bnVsbCwidG8iOjE1NTE2fcaa" \
               "DBd7ImZyb20iOjAsInRvIjoyNzAwMDAwfQ&"

    def get_yug_auto_expert_url(self):
        return f"https://yug-avto-expert.ru/cars/{self.car.condition}/"

    def get_auto_ru_url(self):
        return "https://auto.ru/krasnodar/cars/" \
               f"{self.car.brand}/" \
               f"{self.car.model}/" \
               f"{self.car.generation}/" \
               f"{self.car.condition}/" \
               f"?year_from={self.car.minyear}" \
               f"&year_to={self.car.maxyear}" \
               f"&price_to={self.car.maxprice}" \
               f"&km_age_to={self.car.maxprobeg}" \
               f"&with_discount=false" \
               f"&transmission=ROBOT&transmission=AUTOMATIC&transmission=VARIATOR&transmission=AUTO" \
               f"&steering_wheel=LEFT"

    def get_drom_url(self):
        return "https://krasnodar.drom.ru/" \
               f"{self.car.brand}/" \
               f"{self.car.model}/" \
               f"{self.car.condition}/" \
               f"?maxprice={self.car.maxprice}" \
               f"&minyear={self.car.minyear}" \
               f"&maxyear={self.car.maxyear}" \
               f"&transmission[]=2&transmission[]=3&transmission[]=4&transmission[]=5&transmission[]=-1&ph=1&pts=" \
               f"2&damaged=2&w=2" \
               f"&unsold=1" \
               f"&maxprobeg={self.car.maxprobeg}"
