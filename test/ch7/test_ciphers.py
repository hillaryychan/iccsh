from src.ch7.ciphers import (shift_cipher,
                             vigenere_cipher)


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
