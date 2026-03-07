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


if __name__ == "__main__":
    with open(r"C:\Users\usger\PycharmProjects\APP\data\operations.json", "r", encoding="utf-8") as f:
        transactions = json.load(f)
    filter_trans = filter_transactions_by_state(transactions, "executed")
    pprint(filter_trans)
