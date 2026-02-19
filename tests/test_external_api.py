import unittest
from unittest.mock import Mock, patch
from src.external_api import get_currency_rate, API_KEY


class TestExternalAPI(unittest.TestCase):
    @patch("src.external_api.requests.get")
    def test_get_currency_rate_usd(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 76.754206}
        mock_get.return_value = mock_response

        transaction = [
            {"operationAmount": {"amount": "1000.0", "currency": {"code": "USD"}}}
        ]

        result = get_currency_rate(transaction)

        print(result, type(result))

        self.assertAlmostEqual(result, 76.754206)

        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1000.0",
            headers={"apikey": API_KEY}
        )

    def test_get_currency_rate_rub(self):
        transaction = {"operationAmount": {"amount": "500.0", "currency": {"code": "RUB"}}}
        result = get_currency_rate(transaction)
        self.assertEqual(result, 500.0)


if __name__ == "__main__":
    unittest.main()
