from fractions import Fraction
from src.ch3.kraft_mcmillan import (
    eval_kraft_mcmillan,
    eval_kraft_mcmillan_length,
    eval_kraft_mcmillan_min_length,
    eval_kraft_mcmillan_radix,
)


def test_kraft_mcmillan():
    assert eval_kraft_mcmillan(2, 1, 2, 3, 3, 3) == Fraction(9, 8)
    assert eval_kraft_mcmillan(2, 2, 2, 3, 3, 4, 4, 4) == Fraction(15, 16)
    assert eval_kraft_mcmillan(3, 1, 2, 3, 3, 3, 3, 3, 3, 3) == Fraction(19, 27)
    assert eval_kraft_mcmillan(3, 1, 1, 2, 2, 3, 3, 3, 3) == Fraction(28, 27)


def test_kraft_mcmillan_length():
    assert eval_kraft_mcmillan_length(Fraction(63, 64), 2, 1, 2, 4, 5, 6) == 3
    assert eval_kraft_mcmillan_length(Fraction(7, 8), 2, 2, 2, 3, 4, 4) == 3


def test_kraft_mcmillan_min_length():
    assert eval_kraft_mcmillan_min_length(2, 1, 2, 3, 4, 5, 7) == 6
    assert eval_kraft_mcmillan_min_length(2, 1, 2, 3, 4, 6, 6) == 5


def test_kraft_mcmillan_radix():
    assert eval_kraft_mcmillan_radix(2, 2, 2, 3, 4, 5) == 2
    assert eval_kraft_mcmillan_radix(1, 1, 2, 2, 3, 3, 5) == 3
