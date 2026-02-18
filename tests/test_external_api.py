import unittest
from unittest.mock import Mock, patch
from src.utils import transaction_amount
from src.external_api import get_currency_rate, API_KEY


class TestExternalAPI(unittest.TestCase):
    @patch("src.external_api.requests.get")
    def test_get_currency_rate(self, mock_get):

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"result": 76.754206, "success": True}
        mock_get.return_value = mock_response

        transactions = [
            {"operationAmount": {"amount": "1000", "currency": {"code": "USD"}}},
            {"operationAmount": {"amount": "500", "currency": {"code": "RUB"}}}
        ]

        result = get_currency_rate(transactions)


        self.assertEqual(len(result), 2)
        self.assertAlmostEqual(result[0], 1000 * 76.754206)
        self.assertEqual(result[1], 500)

        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1000",
            headers={"apikey": API_KEY}
        )


if __name__ == "__main__":
    unittest.main()
