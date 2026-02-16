import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')


def get_currency_rate(currency_code: str, amount: float) -> float:
    """ Функция конвертирует сумму операции в разные валюты """
    url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}'
    payload = {}
    headers = {
        "apikey": f'{API_KEY}'
    }

    response = requests.get(url, headers=headers, data=payload)

    result = response.json()
    return float(result['result'])
