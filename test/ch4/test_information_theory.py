from fractions import Fraction
from math import isclose

from src.ch4.information_theory import (
    calculate_entropy,
    calculate_shannon_fano_avg_len,
    shannon_fano_table,
)


def test_calculate_entropy():
    probabilities = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    assert isclose(calculate_entropy(2, probabilities), 1.459147917)

    probabilities = [
        Fraction(27, 40),
        Fraction(9, 40),
        Fraction(3, 40),
        Fraction(1, 40),
    ]
    assert isclose(calculate_entropy(2, probabilities), 1.280273718)

    probabilities = [
        Fraction(0.22),
        Fraction(0.20),
        Fraction(0.18),
        Fraction(0.15),
        Fraction(0.10),
        Fraction(0.08),
        Fraction(0.05),
        Fraction(0.02),
    ]
    assert isclose(calculate_entropy(4, probabilities), 1.376743155)


def test_shannon_fano_table():
    probabilities = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    expected = [
        (Fraction(1, 2), Fraction(2, 1), 1),
        (Fraction(1, 3), Fraction(3, 1), 2),
        (Fraction(1, 6), Fraction(6, 1), 3),
    ]
    assert shannon_fano_table(2, probabilities) == expected

    probabilities = [
        Fraction(27, 40),
        Fraction(9, 40),
        Fraction(3, 40),
        Fraction(1, 40),
    ]
    expected = [
        (Fraction(27, 40), Fraction(40, 27), 1),
        (Fraction(9, 40), Fraction(40, 9), 3),
        (Fraction(3, 40), Fraction(40, 3), 4),
        (Fraction(1, 40), Fraction(40, 1), 6),
    ]
    assert shannon_fano_table(2, probabilities) == expected


def test_shannon_fano_avg_len():
    probabilities = [Fraction(1, 2), Fraction(1, 3), Fraction(1, 6)]
    assert calculate_shannon_fano_avg_len(2, probabilities) == Fraction(5, 3)

    probabilities = [
        Fraction(1, 3),
        Fraction(1, 4),
        Fraction(1, 6),
        Fraction(3, 20),
        Fraction(1, 10),
    ]
    assert calculate_shannon_fano_avg_len(3, probabilities) == Fraction(53, 30)
