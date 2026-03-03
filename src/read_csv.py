import pandas as pd


def transactions_csv_to_dict(file_path: str) -> list[dict]:
    """Чтение данных из .csv и вывод в виде списка словарей"""
    transactions_reviews = pd.read_csv(file_path)
    return transactions_reviews.to_dict(orient="records")


if __name__ == "__main__":
    csv_data = transactions_csv_to_dict("../data/transactions.csv")
    print(csv_data)
