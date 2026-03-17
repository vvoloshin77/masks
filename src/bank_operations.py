from collections import Counter


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""
    descriptions = [operation["description"] for operation in data if operation["description"] in categories]
    op_count = Counter(descriptions)
    return dict(op_count)
