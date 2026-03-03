import json
import logging
import os
from pprint import pprint

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log", mode="w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def transaction_amount(path: str) -> list[dict]:
    """Функция принимает путь до JSON-файла и возвращает список транзакций"""
    try:
        absolute_path = os.path.abspath(path)
        with open(absolute_path, encoding="utf-8") as operations_file:
            try:
                operations_data = json.load(operations_file)
                if isinstance(operations_data, list):
                    logger.info("Успешная проверка на тип")
                    return operations_data
                return []
            except json.JSONDecodeError:
                logger.error("Ошибка декодирования файла")
                print("Ошибка декодирования файла")
    except FileNotFoundError:
        logger.error("Ошибка декодирования файла")
        print("Файл не найден")

    return []


if __name__ == "__main__":  # pragma: no cover
    transactions = transaction_amount("../data/operations.json")
    pprint(transactions)
