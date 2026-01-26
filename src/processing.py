from typing import Any


def filter_by_state(data: list[dict[str, Any]], state="EXECUTED") -> list[dict[str, Any]]:
    """Выводит словари, которые содержат указанный ключ"""

    result = []

    for item in data:
        if item.get("state") == state:
            result.append(item)

    return result


def sort_by_date(data: list[dict[str, Any]], reverse=True) -> list[dict[str, Any]]:
    """Функция возвращает отсортированный по дате список"""

    return sorted(data, key=lambda x: x["date"], reverse=reverse)


if __name__ == '__main__':
    print(filter_by_state([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
    print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}, {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}, {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
