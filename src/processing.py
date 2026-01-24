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
