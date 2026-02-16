from src.external_api import get_currency_rate
from src.utils import transaction_amount
from pprint import pprint

if __name__ == '__main__':  # pragma: no cover
    rate = get_currency_rate(amount=1000, currency_code="USD")
    pprint(rate)

if __name__ == '__main__':  # pragma: no cover
    transactions = transaction_amount('../data/operations.json')
    pprint(transactions)
