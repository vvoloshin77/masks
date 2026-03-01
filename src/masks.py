import logging

# import os

# if not os.path.exists('logs'):
# os.makedirs('logs')


logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/masks.log", mode="w", encoding="UTF-8")
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(card_number: int) -> str:
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
# """Второй варинт реализации функциий на вход принмает номер карты в виде число и возвращает маску"""
# card_number_str = str(card_number).replace(' ', '')
# total_ = card_number_str[:6] + ('*' * 6) + card_number_str[-4:]
# a = []
# for i in range(4):
# a.append(total_[i*4:(i+1)*4])
# return " ".join(a)


# if __name__ == '__main__':
# print(get_mask_card_number(89945678910111213141516))


def get_mask_account(account_number: int) -> str:
    """Функция на вход принмает номер счета в виде число и возвращает маску"""
    account_number_str = str(account_number).replace(" ", "").replace("-", "")
    if len(account_number_str) < 10:
        logger.error("Номер карты введен неверно")
        return "Номер счета введен неверно"
    else:
        logger.info("Функция работает корректно, номер маскируется")
        return f"**{account_number_str[-4:]}"


if __name__ == "__main__":  # pragma: no cover
    print(get_mask_account(89945678910111213141516))
    print(get_mask_card_number(8994567891011123099905558))
