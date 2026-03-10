import logging
import json
from pprint import pprint

# import os

# if not os.path.exists('logs'):
# os.makedirs('logs')


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler(r"C:\Users\usger\PycharmProjects\APP\logs\masks.log", mode="w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: str) -> str:
    """Функция на вход принмает номер карты в виде число и возвращает маску"""
    card_number_str = str(card_number).replace(" ", "").replace("-", "")
    if len(card_number_str) < 16:
        logger.error("Номер карты введен неверно")
        return "Номер карты введен неверно"
    if len(card_number_str) == 16:
        logger.info("Функция работает корректно, номер маскируется")
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    else:
        logger.info("Функция работает корректно, номер маскируется")
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


# def get_mask_card_number(card_number: int) -> str:
#     """Второй варинт реализации функциий на вход принмает номер карты в виде число и возвращает маску"""
#     card_number_str = str(card_number).replace(' ', '')
#     total_ = card_number_str[:6] + ('*' * 6) + card_number_str[-4:]
#     a = []
#     for i in range(4):
#         a.append(total_[i*4:(i+1)*4])
#     return " ".join(a)
# if __name__ == '__main__':
# print(get_mask_card_number(89945678910111213141516))


def get_mask_account(account_number: str) -> str:
    """Функция на вход принмает номер счета в виде число и возвращает маску"""
    account_number_str = str(account_number).replace(" ", "").replace("-", "")
    if len(account_number_str) < 10:
        logger.error("Номер карты введен неверно")
        return "Номер счета введен неверно"
    else:
        logger.info("Функция работает корректно, номер маскируется")
        return f"**{account_number_str[-4:]}"


def get_mask_payment(payment_info: str) -> str:
    """Функция разделяет строку на номер и название, маскирует название"""
    if not payment_info:
        logger.error("Not valid data")
        return ""

    parts = payment_info.split()
    number = parts[-1]
    name = ' '.join(parts[:-1])

    if "Счет" in name:
        logger.info("Функция работает корректно, выводит Счет и маску")
        return f'{name} {get_mask_account(number)}'
    else:
        logger.info("Функция работает корректно, выводит название платежной системы и маску")
        return f'{name} {get_mask_card_number(number)}'


if __name__ == "__main__":  # pragma: no cover
    with open(r"C:\Users\usger\PycharmProjects\APP\data\operations.json", "r", encoding="utf-8") as f:
        transactions = json.load(f)

    for transaction in transactions:
        if not transaction:
            continue
        raw_from = transaction.get("from", "")
        raw_to = transaction.get("to", "")

        sender_masked = get_mask_payment(raw_from)
        recipient_masked = get_mask_payment(raw_to)

        if sender_masked:
            print(f'{sender_masked} -> {recipient_masked}')
        else:
            print(f'{recipient_masked}')
