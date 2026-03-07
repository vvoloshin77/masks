import re


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """Функцию принимает список словарей с данными о банковских операциях и строку поиска, а возвращает список словарей, у которых есть данная строка"""
    result = []
    for operation in data:
        if re.search(search, operation["description"]):
            result.append(operation)
    return result
