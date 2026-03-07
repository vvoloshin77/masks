import json
from pprint import pprint


def filter_transactions_by_state(transactions: list[dict], status: str) -> list[dict]:
    """Функция фильтрации операций по статусу"""
    # with open(file_path, "r", encoding="utf-8") as f:
    #     transactions = json.load(f)

    statuses = ["EXECUTED", "CANCELED", "PENDING"]

    if status.upper() not in statuses:
        print(f"\nНекорректный статус: {status}.\nДоступные статусы: {statuses}.\n")
        return []

    return [t for t in transactions if "state" in t and str(t["state"]).upper() == status.upper()]


def filter_transactions_by_date(transactions: list[dict], ascending: bool = False) -> list[dict]:
    """ Функция фильтрации операций по дате """
    filtered_data = [t for t in transactions if 'date' in t]
    return sorted(filtered_data, key=lambda x: x['date'], reverse=not ascending)


def filter_transactions_by_keyword(transactions: list[dict], keyword: str) -> list[dict]:
    """ Функция фильтрации операций по слову в описании """
    filtered_data = [t for t in transactions if 'description' in t and keyword.lower() in t['description'].lower()]
    return sorted(filtered_data, key=lambda x: x['description'])


if __name__ == "__main__":
    with open(r"C:\Users\usger\PycharmProjects\APP\data\operations.json", "r", encoding="utf-8") as f:
        transactions = json.load(f)
    filter_trans = filter_transactions_by_state(transactions, "executed")
    pprint(filter_trans)

    sort_trans = filter_transactions_by_date(filter_trans)
    pprint(sort_trans)

    sort_word = filter_transactions_by_keyword(filter_trans, 'перевод организации')
    pprint(sort_word)
