import pytest

from numpy.testing import assert_almost_equal
from src.compression import (comma_encode,
                             lz78_encode,
                             lz78_decode,
                             validate_arithmetic_symbols,
                             arithmetic_encode,
                             arithmetic_decode)


def test_comma_encode():
    assert comma_encode(4, '31415') == '1100111001111'
    assert comma_encode(4, '21252') == '10010111110'


def test_lz78_encode():
    assert lz78_encode('bccbcbacbabcbac') == [('b', (0, 'b')),
                                              ('c', (0, 'c')),
                                              ('cb', (2, 'b')),
                                              ('cba', (3, 'a')),
                                              ('cbab', (4, 'b')),
                                              ('cbac', (4, 'c'))]

    assert lz78_encode('caaaabaaaaaab') == [('c', (0, 'c')),
                                            ('a', (0, 'a')),
                                            ('aa', (2, 'a')),
                                            ('ab', (2, 'b')),
                                            ('aaa', (3, 'a')),
                                            ('aaab', (5, 'b'))]


def test_lz78_decode():
    outputs = [(0, 'c'), (1, 'c'), (2, 'b'), (3, 'c'), (3, 'b'), (4, 'a')]
    assert lz78_decode(outputs) == 'cccccbccbcccbbccbca'

    outputs = [(0, 'b'), (1, 'b'), (2, 'c'), (3, 'a'), (4, 'b'), (5, 'b')]
    assert lz78_decode(outputs) == 'bbbbbcbbcabbcabbbcabb'


def test_validate_arithmetic_symbols_with_varying_source_and_probabilities():
    with pytest.raises(ValueError) as exc:
        validate_arithmetic_symbols(['a', '.'], [0.3, 0.3, 0.4])
    assert str(exc.value) == ("No. of symbols and probabilities do not match\n"
                              "source: ['a', '.']\n"
                              "probabilities: [0.3, 0.3, 0.4]")

    with pytest.raises(ValueError) as exc:
        validate_arithmetic_symbols(['a', 'b', '.'], [0.8, 0.2])
    assert str(exc.value) == ("No. of symbols and probabilities do not match\n"
                              "source: ['a', 'b', '.']\n"
                              "probabilities: [0.8, 0.2]")


def test_validate_arithmetic_symbols_with_invalid_probabilities():
    with pytest.raises(ValueError) as exc:
        validate_arithmetic_symbols(['a', 'b', '.'], [0.3, 0.2, 0.1])
    assert str(exc.value) == "Probabilities [0.3, 0.2, 0.1] do not sum to 1"


def test_arithmetic_encode():
    result = arithmetic_encode(['a', 'b', '.'], [0.6, 0.2, 0.2], "baa.")
    assert_almost_equal(result, 0.6648)

    result = arithmetic_encode(['a', 'b', '.'], [0.4, 0.3, 0.3], "baa.")
    assert_almost_equal(result, 0.4408)


def test_arithmetic_encode_with_extra_symbols():
    with pytest.raises(ValueError) as exc:
        arithmetic_encode(['a', '.'], [0.5, 0.5], 'ab.')
    assert str(exc.value) == ("Message 'ab.' contains symbol(s) not in source "
                              "symbols ['a', '.']")


def test_arithmetic_decode():
    message = arithmetic_decode(['a', 'b', 'c', '.'],
                                [0.4, 0.3, 0.2, 0.1],
                                0.12345)
    assert message == 'aacac.'

    message = arithmetic_decode(['a', 'b', '.'], [0.8, 0.1, 0.1], 0.7008)
    assert message == 'aba.'
