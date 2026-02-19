import os
import requests
from pprint import pprint
from utils import transaction_amount
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_currency_rate(transaction_list: list[dict]) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции"""

    data = transaction_list[1]

    currency_code = data['operationAmount']['currency']['code']
    op_amount = float(data['operationAmount']['amount'])

    if currency_code != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={op_amount}"
        headers = {"apikey": f"{API_KEY}"}

        response = requests.get(url, headers=headers)

        result = response.json()
        return result
    else:
        return op_amount


if __name__ == "__main__":  # pragma: no cover
    transactions = transaction_amount("../data/operations.json")
    rate = get_currency_rate(transactions)
    pprint(rate)
