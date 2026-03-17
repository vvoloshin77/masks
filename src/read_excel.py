import pandas as pd


def transactions_excel_to_dict(file_path: str) -> list[dict]:
    """Чтение данных из .xlsx и вывод в виде списка словарей"""
    transactions_reviews = pd.read_excel(file_path, engine="openpyxl")
    return transactions_reviews.to_dict(orient="records")


if __name__ == "__main__":
    excel_data = transactions_excel_to_dict(r"C:\Users\usger\PycharmProjects\APP\data\transactions_excel.xlsx")
    print(excel_data)
