import os
import requests
from services.redis_service import RedisConnect


def _get_chat_ids(token: str):
    chats_raw = requests.get(f"https://api.telegram.org/bot{token}/getUpdates").json()['result']
    return set([chat_id['message']['chat']['id'] for chat_id in chats_raw])


def _preparing_ad_format(car):
    return f"Новое объявление: \n\n"\
        f"{car['image']}\n"\
        f"Мощность -> {car['power']}\n"\
        f"Цена -> {car['price']}\n"\
        f"Пробег -> {car['distance']}\n"\
        f"Год -> {car['year']}\n"


def public_ad_in_telegram(cars):
    redis_connect = RedisConnect()

    for car in cars:
        if car['hash'] not in redis_connect.get_all_keys():
            send_result_to_telegram(_preparing_ad_format(car))
            redis_connect.redis_set(car['hash'])
            print('Database was updated')


def send_result_to_telegram(text: str):
    token = os.environ['API_TOKEN']

    url = f"https://api.telegram.org/bot{token}"
    send_message = f"{url}/sendMessage"
    for chat_id in _get_chat_ids(token):
        requests.post(
            send_message,
            data={"chat_id": chat_id, "text": text}
        )
