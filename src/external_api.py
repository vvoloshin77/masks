import os
from pprint import pprint

import requests
from dotenv import load_dotenv

from src.utils import transaction_amount

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_currency_rate(transaction: dict) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции"""


    currency_code = transaction['operationAmount']['currency']['code']
    op_amount = float(transaction['operationAmount']['amount'])

    if currency_code != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={op_amount}"
        headers = {"apikey": f"{API_KEY}"}

        response = requests.get(url, headers=headers)

        result = response.json()
        return result

    return op_amount


if __name__ == "__main__":  # pragma: no cover
    transactions = transaction_amount("../data/operations.json")
    rate = get_currency_rate(transactions[0])
    pprint(rate)
