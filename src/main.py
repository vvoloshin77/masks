from src.external_api import get_currency_rate
from pprint import pprint

if __name__ == '__main__': # pragma: no cover
    rate = get_currency_rate(amount=1000, currency_code="USD")
    pprint(rate)