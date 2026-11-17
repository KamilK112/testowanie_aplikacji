import pytest
from kalkulator import oblicz_srednia


def test_srednia_zwyklych_liczb():
    assert oblicz_srednia([10, 20, 30]) == 20


def test_srednia_jednej_liczby():
    assert oblicz_srednia([5]) == 5


def test_srednia_liczb_dziesietnych():
    assert oblicz_srednia([2.5, 3.5]) == 3


def test_pusta_lista():
    with pytest.raises(ValueError):
        oblicz_srednia([])
