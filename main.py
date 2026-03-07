from pprint import pprint
from src.utils import transaction_amount
from src.read_csv import transactions_csv_to_dict
from src.read_excel import transactions_excel_to_dict
from src.filter_transaction import filter_transactions_by_state


def main():
    """ Функция отвечает за основную логику проекта и связывает функциональности между собой """
    greetings = """
    Привет! Добро пожаловать в программу работы с банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
    """
    print(greetings)


    while True:
        user_choice = input('Пользователь: ')
        if user_choice == '1':
            transactions = transaction_amount(r"C:\Users\usger\PycharmProjects\APP\data\operations.json")
            print(f'\nПункт: {user_choice}, для обработки выбран JSON-файл.\n')
            break
        elif user_choice == '2':
            transactions = transactions_csv_to_dict(r"C:\Users\usger\PycharmProjects\APP\data\transactions.csv")
            print(f'\nПункт: {user_choice}, для обработки выбран CSV-файл.\n')
            break
        elif user_choice == '3':
            transactions = transactions_excel_to_dict(
                r"C:\Users\usger\PycharmProjects\APP\data\transactions_excel.xlsx")
            print(f'\nПункт: {user_choice}, для обработки выбран XLSX-файл.\n')
            break
        else:
            print(f'\nНеверный пункт меню. Попробуйте выбрать снова.\n')

    statuses = ['EXECUTED', 'CANCELED', 'PENDING']

    while True:
        status = input(f'Доступные для фильтровки статусы: {", ".join(statuses)}\n'
                       f'\nВведите статус, по которому необходимо выполнить фильтрацию: ').upper()
        if status in statuses:
            print(f'\nОперации отфильтрованы по статусу: {status}\n')
            filtered_transactions = filter_transactions_by_state(transactions, status)
            pprint(filtered_transactions)
            break
        else:
            print(f"Статус операции: '{status}', некорректный.\n")


if __name__ == '__main__':  # pragma: no cover
    main()
