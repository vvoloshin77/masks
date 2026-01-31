import pytest


from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('number_card, expected', [
    ('Счет 64686473678894779589', 'Счет **9589'),
    ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229'),
])
def test_mask_account_card(number_card, expected):
    assert mask_account_card(number_card) == expected


@pytest.mark.parametrize('date, expected', [
    ('2024-03-11T02:26:18.671407', '03.11.2024')
])
def test_get_date(date, expected):
    assert get_date(date) == expected


