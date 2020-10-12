from fractions import Fraction
from src.compression import eval_kraft_mcmillan


def test_kraft_mcmillan():
    assert eval_kraft_mcmillan(2, 1, 2, 3, 3, 3) == Fraction(9, 8)
    assert eval_kraft_mcmillan(2, 2, 2, 3, 3, 4, 4, 4) == Fraction(15, 16)
    assert eval_kraft_mcmillan(3, 1, 2, 3, 3, 3, 3, 3, 3, 3) == Fraction(19, 27)
    assert eval_kraft_mcmillan(3, 1, 1, 2, 2, 3, 3, 3, 3) == Fraction(28, 27)
