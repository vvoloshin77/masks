# from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(number_input: str) -> str:
    """Функция на вход принмает номер карты и счета в виде число и возвращает их маски"""
    number_input_str = str(number_input).replace(" ", "")

    key_words = ["MasterCard", "Maestro", "Visa Platinum", "Visa Classic", "Visa Gold"]

    for word in key_words:
        if word in number_input:
            return f"{word} {number_input_str[-16:-12]} {number_input_str[-12:-10]}** **** {number_input_str[-4:]}"
        elif "Счет" in number_input:
            return f"Счет **{number_input_str[-4:]}"


def get_date(date_input: str) -> str:
    """Функция принимает на вход строку с датой, возвращает только дату в стандартном формате"""
    date_input_str = str(date_input).replace(" ", "").replace(":", "").replace("-", "").replace(".", "")
    return f"{date_input_str[4:6]}.{date_input_str[6:8]}.{date_input_str[:4]}"


#if __name__ == "__main__":
    #print(mask_account_card("Счет 64686473678894779589"))
    #print(mask_account_card("Visa Platinum 8990922113665229"))
    #print(get_date("2024-03-11T02:26:18.671407"))
