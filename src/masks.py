def get_mask_card_number(card_number: int) -> str:
    """Функция на вход принмает номер карты в виде число и возвращает маску"""
    card_number_str = str(card_number).replace(" ", "")
    if len(card_number_str) < 16:
        return "Номер карты введен неверно"
    if len(card_number_str) == 16:
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    else:
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(8994567891011123099905558))


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
    account_number_str = str(account_number).replace(" ", "")
    return f"**{account_number_str[-4:]}"


if __name__ == "__main__":
    print(get_mask_account(89945678910111213141516))
