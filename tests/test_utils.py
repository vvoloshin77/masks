import unittest
from unittest.mock import patch, mock_open
from src.utils import transaction_amount


mock_data = '[{"date": "2019-01-05T00:52:30.108534", "description": "Перевод со счета на счет", "from": "Счет 46363668439560358409", "id": 957763565, "operationAmount": {"amount": "87941.37", "currency": {"code": "RUB", "name": "руб."}}, "state": "EXECUTED", "to": "Счет 96527012349577388612"}]'


class TestTransactionAmount(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=mock_data)
    def test_transaction_amount(self, mock_file):
        expected_result = [{
            'date': '2019-01-05T00:52:30.108534',
            'description': 'Перевод со счета на счет',
            'from': 'Счет 46363668439560358409',
            'id': 957763565,
            'operationAmount': {'amount': '87941.37',
                                'currency': {'code': 'RUB', 'name': 'руб.'}},
            'state': 'EXECUTED',
            'to': 'Счет 96527012349577388612'}]
        with patch('builtins.open', mock_open(read_data=mock_data)):
            result = transaction_amount('test_path')
            self.assertEqual(result, expected_result)
