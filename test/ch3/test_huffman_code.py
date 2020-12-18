import pytest

from fractions import Fraction
from src.ch3.huffman_code import calculate_huffman_avg_len, generate_huffman


def test_calculate_avg_huffman_len():
    probabilities = [Fraction(7, 10), Fraction(1, 5), Fraction(1, 10)]
    avg_len = calculate_huffman_avg_len(2, probabilities)
    assert avg_len == Fraction(13, 10)

    probabilities = [
        Fraction(27, 64),
        Fraction(9, 64),
        Fraction(9, 64),
        Fraction(9, 64),
        Fraction(3, 64),
        Fraction(3, 64),
        Fraction(3, 64),
        Fraction(1, 64),
    ]
    avg_len = calculate_huffman_avg_len(3, probabilities)
    assert avg_len == Fraction(105, 64)

    probabilities = [
        Fraction(6, 17),
        Fraction(5, 17),
        Fraction(2, 17),
        Fraction(2, 17),
        Fraction(2, 17),
    ]
    avg_len = calculate_huffman_avg_len(4, probabilities)
    assert avg_len == Fraction(21, 17)


def test_calculate_avg_huffman_len_with_invalid_probabilities():
    with pytest.raises(ValueError) as exc:
        probabilities = [
            Fraction(4, 11),
            Fraction(2, 11),
            Fraction(1, 11),
            Fraction(1, 11),
            Fraction(1, 11),
            Fraction(1, 11),
        ]
        calculate_huffman_avg_len(3, probabilities)
    assert str(exc.value) == (
        "Probabilities ['4/11', '2/11', '1/11', '1/11', "
        "'1/11', '1/11'] do not sum to 1"
    )


def test_generate_huffman_with_fractions():
    probabilities = [
        Fraction(3, 10),
        Fraction(2, 10),
        Fraction(2, 10),
        Fraction(1, 10),
        Fraction(1, 10),
        Fraction(1, 10),
    ]
    result = generate_huffman(2, probabilities)
    assert result == [
        (1, Fraction(3, 10), "01"),
        (2, Fraction(2, 10), "11"),
        (3, Fraction(2, 10), "000"),
        (4, Fraction(1, 10), "001"),
        (5, Fraction(1, 10), "100"),
        (6, Fraction(1, 10), "101"),
    ]

    probabilities = [
        Fraction(1, 3),
        Fraction(1, 3),
        Fraction(1, 9),
        Fraction(1, 9),
        Fraction(1, 27),
        Fraction(1, 27),
        Fraction(1, 27),
    ]
    result = generate_huffman(3, probabilities)
    assert result == [
        (1, Fraction(1, 3), "1"),
        (2, Fraction(1, 3), "2"),
        (3, Fraction(1, 9), "01"),
        (4, Fraction(1, 9), "02"),
        (5, Fraction(1, 27), "000"),
        (6, Fraction(1, 27), "001"),
        (7, Fraction(1, 27), "002"),
    ]


def test_genrate_huffman_with_decimals():
    probabilities = [0.7, 0.2, 0.1]
    result = generate_huffman(2, probabilities)
    assert result == [
        (1, Fraction(0.7), "0"),
        (2, Fraction(0.2), "10"),
        (3, Fraction(0.1), "11"),
    ]

    probabilities = [0.22, 0.20, 0.18, 0.15, 0.1, 0.08, 0.05, 0.02]
    result = generate_huffman(4, probabilities)
    assert result == [
        (1, Fraction(0.22), "1"),
        (2, Fraction(0.20), "2"),
        (3, Fraction(0.18), "3"),
        (4, Fraction(0.15), "00"),
        (5, Fraction(0.1), "01"),
        (6, Fraction(0.08), "02"),
        (7, Fraction(0.05), "030"),
        (8, Fraction(0.02), "031"),
    ]


def test_generate_huffman_random_probability_order():
    probabilities = [0.2, 0.6, 0.2]
    result = generate_huffman(2, probabilities)
    assert result == [
        (1, Fraction(0.2), "10"),
        (2, Fraction(0.6), "0"),
        (3, Fraction(0.2), "11"),
    ]

    probabilities = [0.1, 0.4, 0.5]
    result = generate_huffman(2, probabilities)
    assert result == [
        (1, Fraction(0.1), "01"),
        (2, Fraction(0.4), "00"),
        (3, Fraction(0.5), "1"),
    ]


def test_generate_huffman_with_invalid_probabilities():
    with pytest.raises(ValueError) as exc:
        probabilities = [
            Fraction(4, 11),
            Fraction(2, 11),
            Fraction(1, 11),
            Fraction(1, 11),
            Fraction(1, 11),
            Fraction(1, 11),
        ]
        generate_huffman(3, probabilities)
    assert str(exc.value) == (
        "Probabilities ['4/11', '2/11', '1/11', '1/11', "
        "'1/11', '1/11'] do not sum to 1"
    )
