import traceback
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """Функция на вход принимает файл"""

    def decorator(func: Callable) -> Callable:
        """Функция на вход принимает функцию"""

        def wrapper(*args: Any, **kwargs: Any) -> Any:
            """Функция на вход принимает параметры"""
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message)
            except Exception:
                error_type = traceback.format_exc().strip().split("\n")[-1]
                log_message = f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}\n"
                result = None
                if filename:
                    with open(filename, "a") as f:
                        f.write(log_message)
                else:
                    print(log_message)
            return result

        return wrapper

    return decorator


@log(filename=None)
def my_function(x: int, y: int) -> int:
    return x + y


print(my_function("", 2))
