import pytest

from src.decorators import my_function


def test_log(capsys):
    my_function(2, 2)
    captured = capsys.readouterr()
    assert captured.out.strip() == 'my_function ok'