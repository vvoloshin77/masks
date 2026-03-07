# import pandas as pd
#
#
# def transactions_csv_to_dict(file_path: str) -> list[dict]:
#     """Чтение данных из .csv и вывод в виде списка словарей"""
#     transactions_reviews = pd.read_csv(file_path)
#     return transactions_reviews.to_dict(orient="records")
#
#
# if __name__ == "__main__":
#     csv_data = transactions_csv_to_dict(r"C:\Users\usger\PycharmProjects\APP\data\transactions.csv")
#     print(csv_data)

import csv
from pprint import pprint


def transactions_csv_to_dict(file_path: str) -> list[dict]:
    """Читает CSV-файл и возвращает список словарей"""
    transactions = []

    with open(file_path, "r", encoding="utf-8") as f:
        # Указываем разделитель ';' вместо ',' (по умолчанию)
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            transactions.append(row)

    return transactions


if __name__ == "__main__":  # pragma: no cover
    trans = transactions_csv_to_dict(r"C:\Users\usger\PycharmProjects\APP\data\transactions.csv")
    pprint(trans[0] if trans else "Нет данных")
