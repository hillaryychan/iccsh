from fractions import Fraction
from math import isclose

from src.ch4.information_theory import calculate_entropy


def test_calculate_entropy():
    probabilities = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    assert isclose(calculate_entropy(2, probabilities), 1.459147917)

    probabilities = [Fraction(27, 40), Fraction(9, 40),
                     Fraction(3, 40), Fraction(1, 40)]
    assert isclose(calculate_entropy(2, probabilities), 1.280273718)

    probabilities = [Fraction(0.22), Fraction(0.20), Fraction(0.18),
                     Fraction(0.15), Fraction(0.10), Fraction(0.08),
                     Fraction(0.05), Fraction(0.02)]
    assert isclose(calculate_entropy(4, probabilities), 1.376743155)
