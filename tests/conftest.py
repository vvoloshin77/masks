import pytest


@pytest.fixture
def card_number():
    return '8994 56** **** 5558'


@pytest.fixture
def account_number():
    return '**1516'


@pytest.fixture
def number_card():
    return 'Счет **9589', 'Visa Platinum 8990 92** **** 5229'


@pytest.fixture
def date():
    return '03.11.2024'
