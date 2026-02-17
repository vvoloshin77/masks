import unittest
from unittest.mock import Mock, patch

from src.external_api import API_KEY, get_currency_rate


class TestExternalAPI(unittest.TestCase):
    @patch("src.external_api.requests.get")
    def test_get_currency_rate(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"result": 76754.206, "success": True}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        result = get_currency_rate(amount=1000, currency_code="USD")
        self.assertEqual(result, 76754.206)
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1000",
            headers={"apikey": API_KEY},  # API_KEY из .env не загрузится в тесте
            data={},
        )


if __name__ == "__main__":
    unittest.main()
