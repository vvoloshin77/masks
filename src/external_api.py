import os
import requests
from pprint import pprint
from utils import transaction_amount
from dotenv import load_dotenv
import time

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_currency_rate(transaction_list: list[dict]) -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции"""

    transactions_in_rub = []
    for transaction in transaction_list[:2]:
        operation_amount = transaction.get("operationAmount")

        if not operation_amount:
            continue
        amount = float(operation_amount["amount"])
        currency_code = operation_amount["currency"]["code"]

        if currency_code == "RUB":
            transactions_in_rub.append(amount)
        else:
            url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
            headers = {"apikey": f"{API_KEY}"}

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                result = response.json()
                transactions_in_rub.append(result["result"])

            elif response.status_code == 429:
                print("Rate limit exceeded. Waiting...")
                time.sleep(10)
                continue

            else:
                raise ValueError(f"Error fetching currency rate: {response.status_code}")


    return transactions_in_rub


if __name__ == "__main__":  # pragma: no cover
    transactions = transaction_amount("../data/operations.json")
    rate = get_currency_rate(transactions)
    pprint(rate)
