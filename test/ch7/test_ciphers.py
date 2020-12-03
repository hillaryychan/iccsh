from fractions import Fraction
from math import isclose
from src.ch7.ciphers import (shift_cipher,
                             vigenere_cipher,
                             plaintext_feedback_encode,
                             plaintext_feedback_decode,
                             ciphertext_feedback_encode,
                             ciphertext_feedback_decode,
                             index_of_coincidence,
                             estimate_key_len)


def test_shift_cipher():
    assert shift_cipher(3, 'abcdefghijklm',
                        'nopqrstuvwxyz') == 'defghijklmnop qrstuvwxyzabc'
    assert shift_cipher(-3, 'ABCDEFGHIJKLM',
                        'NOPQRSTUVWXYZ') == 'XYZABCDEFGHIJ KLMNOPQRSTUVW'
    assert shift_cipher(1, 'HeLlo', 'wOrLd') == 'IfMmp xPsMe'
    assert shift_cipher(0, 'greetings') == 'greetings'


def test_vigenere_cipher():
    message = ['THIS', 'IS', 'AN', 'EXAMPLE']
    expected = 'VVLW KG DR GLDQRZH'
    assert vigenere_cipher('CODE', *message, decode=False) == expected

    message = ['KMHZ', 'HTS,', 'Q', 'OWWM', 'APHB', 'FWB', 'KYCZP',
               'APPA', 'LFHU', 'HVK', 'MURVGLL', 'APL', 'KVCYAL!']
    expected = ('DEAR ALL, I HOPE THAT YOU CRUSH '
                'THIS EXAM AND ENJOYED THE COURSE!')
    assert vigenere_cipher('HI', *message, decode=True) == expected


def test_plaintext_feedback_encode():
    message = ['THIS', 'IS', 'AN', 'EXAMPLE']
    expected = 'VVLW BZ IF MPAZTIE'
    assert plaintext_feedback_encode('CODE', *message) == expected


def test_plaintext_feedback_decode():
    message = ['VVLW', 'BZ', 'IF', 'MPAZTIE']
    expected = 'THIS IS AN EXAMPLE'
    assert plaintext_feedback_decode('CODE', *message) == expected

    message = ['IRDBHQIPVPBVKBRQ']
    expected = 'IAMTHEPIRATEKING'
    assert plaintext_feedback_decode('ARR', *message) == expected


def test_ciphertext_feedback_encode():
    message = ['THIS', 'IS', 'AN', 'EXAMPLE']
    expected = 'VVLW DN LJ HKLVWVP'
    assert ciphertext_feedback_encode('CODE', *message) == expected


def test_ciphertext_feedback_decode():
    message = ['VVLW', 'DN', 'LJ', 'HKLVWVP']
    expected = 'THIS IS AN EXAMPLE'
    assert ciphertext_feedback_decode('CODE', *message) == expected


def test_incidence_of_coincidence():
    message = ['KMHZ', 'HTS,' 'Q', 'OWWM', 'APHB', 'FWB', 'KYCZP',
               'APPA', 'LFHU', 'HVK', 'MURVGLL', 'APL', 'KVCYAL!']
    assert index_of_coincidence(*message) == Fraction(61, 1275)
    assert isclose(index_of_coincidence(*message), 0.04784313725490196)


def test_estimate_key_len():
    message = ['KMHZ', 'HTS,' 'Q', 'OWWM', 'APHB', 'FWB', 'KYCZP',
               'APPA', 'LFHU', 'HVK', 'MURVGLL', 'APL', 'KVCYAL!']
    assert isclose(estimate_key_len(*message), 2.8158169193371227)
