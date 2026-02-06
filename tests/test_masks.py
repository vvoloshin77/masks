import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        ("8994567891011123099905558", "8994 56** **** 5558"),
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
        ("1234-5678-1234-5678", "1234 56** **** 5678"),
        ("1234   5678   1234   5678", "1234 56** **** 5678"),
        ("", "Номер карты введен неверно"),
        ("678855885", "Номер карты введен неверно"),
    ],
)
def test_get_mask_card_number(value: int, expected: str) -> str:
    assert get_mask_card_number(value) == expected


# def test_get_mask_card_number(card_number):
# assert get_mask_card_number(8994567891011123099905558) == card_number
# with pytest.raises(ValueError):
# get_mask_card_number(868848488844838)


@pytest.mark.parametrize(
    "value, expected",
    [
        ("89945678910111213141516", "**1516"),
        ("688599399834949", "**4949"),
        ("", "Номер счета введен неверно"),
        ("89048-859980-984980", "**4980"),
        ("90-09-90", "Номер счета введен неверно"),
    ],
)
def test_get_mask_account(value: int, expected: str) -> str:
    assert get_mask_account(value) == expected


# def test_get_mask_account(account_number):
# assert get_mask_account(89945678910111213141516) == account_number
