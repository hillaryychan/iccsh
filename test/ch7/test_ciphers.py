from src.ch7.ciphers import (shift_encode)


def test_shift_encode():
    assert shift_encode(3, 'abcdefghijklm',
                        'nopqrstuvwxyz') == 'defghijklmnop qrstuvwxyzabc'
    assert shift_encode(-3, 'ABCDEFGHIJKLM',
                        'NOPQRSTUVWXYZ') == 'XYZABCDEFGHIJ KLMNOPQRSTUVW'
    assert shift_encode(1, 'HeLlo', 'wOrLd') == 'IfMmp xPsMe'
    assert shift_encode(0, 'greetings') == 'greetings'
