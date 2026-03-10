from src.utils import transaction_amount
from src.masks import get_mask_payment
from src.read_csv import transactions_csv_to_dict
from src.read_excel import transactions_excel_to_dict
from src.filter_transaction import filter_transactions_by_state, filter_transactions_by_date, \
    filter_transactions_by_keyword


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
            break
        else:
            print(f"Статус операции: '{status}', некорректный.\n")

    if filtered_transactions:
        user_sort_choice = input('\nОтсортировать операции по дате ?\nВведите Да/Нет:  ').strip().lower()
        if user_sort_choice == 'да':
            user_order_choice = input(
                '\nОтсортировать по возрастанию или по убыванию ?\nВведите по возрастанию/по убыванию: ').strip().lower()
            ascending = True if 'по возрастанию' in user_order_choice else False
            filtered_transactions = filter_transactions_by_date(filtered_transactions, ascending)

        user_code_choice = input('\nВыводить только рублевые транзакции ?\nВведите Да/Нет:  ').strip().lower()
        if user_code_choice == ['RUB']:
            filtered_transactions = [t for t in transactions if t['currency_code'] == 'RUB']

        user_sort_by_word = input(
            '\nОтфильтровать список транзакций по определенному слову в описании?\nВведите Да/Нет:  ').strip().lower()
        if user_sort_by_word == 'да':
            key_word = input('\nВведите слово для фильтрации:  ')
            filtered_transactions = filter_transactions_by_keyword(filtered_transactions, key_word)

        if filtered_transactions:
            print('\nРаспечатываю итоговый список транзакций...')
            print(f'\nВсего банковских операций в выборке: {len(filtered_transactions)}')

            for transaction in filtered_transactions:
                if not transaction:
                    continue

                raw_from = transaction.get("from", "")
                raw_to = transaction.get("to", "")

                op_amount = transaction.get("operationAmount", {})
                amount = op_amount.get("amount", "")
                currency_data = op_amount.get("currency", {})
                currency_code = currency_data.get("code", "")

                sender_masked = get_mask_payment(raw_from)
                recipient_masked = get_mask_payment(raw_to)

                print(f'\n{transaction["date"][:10]} {transaction["description"]}')
                if sender_masked:
                    print(f'{sender_masked} -> {recipient_masked}')
                else:
                    print(f'{recipient_masked}')
                print(f'Сумма: {amount} {currency_code}')
        else:
            print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')


if __name__ == '__main__':  # pragma: no cover
    main()
