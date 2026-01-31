import pytest


@pytest.fixture
def card_number() -> str:
    return "8994 56** **** 5558"


@pytest.fixture
def account_number() -> str:
    return "**1516"


@pytest.fixture
def number_card() -> tuple:
    return "Счет **9589", "Visa Platinum 8990 92** **** 5229"


@pytest.fixture
def date() -> str:
    return "03.11.2024"


@pytest.fixture
def state() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def sort() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
