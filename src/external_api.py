import os
from pprint import pprint

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_currency_rate(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции"""

    currency_code = str(transaction['operationAmount']['currency']['code'])
    op_amount = float(transaction['operationAmount']['amount'])

    if currency_code != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={op_amount}"
        headers = {"apikey": f"{API_KEY}"}

        response = requests.get(url, headers=headers, timeout=10)

        result = response.json()["result"]
        return result

    return op_amount


if __name__ == "__main__":  # pragma: no cover
    x_rub = {
        "id": 121646999,
        "state": "CANCELED",
        "date": "2018-06-08T16:14:59.936274",
        "operationAmount": {
            "amount": "91121.62",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 7552745726849311",
        "to": "Счет 34799481846914116850"
    }

    x_usd = {
        "id": 179194306,
        "state": "EXECUTED",
        "date": "2019-05-19T12:51:49.023880",
        "operationAmount": {
            "amount": "6381.58",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "МИР 5211277418228469",
        "to": "Счет 58518872592028002662"
    }

    pprint(get_currency_rate(x_rub))
    pprint(get_currency_rate(x_usd))
