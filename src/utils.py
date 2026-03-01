import json
import os
from pprint import pprint


def transaction_amount(path: str) -> list[dict]:
    """Функция принимает путь до JSON-файла и возвращает список транзакций"""
    try:
        absolute_path = os.path.abspath(path)
        with open(absolute_path, encoding="utf-8") as operations_file:
            try:
                operations_data = json.load(operations_file)
                if isinstance(operations_data, list):
                    return operations_data
                return []
            except json.JSONDecodeError:
                print("Ошибка декодирования файла")
    except FileNotFoundError:
        print("Файл не найден")
        return []


if __name__ == "__main__":  # pragma: no cover
    transactions = transaction_amount("../data/operations.json")
    pprint(transactions)
