from src.ch7.cryptography import (rsa_exponent_key,
                                  rsa_encrypt,
                                  rsa_decrypt)


def test_rsa_exponent_key():
    assert rsa_exponent_key(10033, 1787) == 11
    assert rsa_exponent_key(10033, 11) == 1787
    assert rsa_exponent_key(551, 55) == 55


def test_rsa_encrypt():
    assert rsa_encrypt(551, 55, 'hi') == '409 182'


def test_rsa_decrypt():
    assert rsa_decrypt(551, 55, 302, 241) == 'OK'
    assert rsa_decrypt(391, 3, 366, 14, 126, 126, 3, 249,
                       258, 126, 148, 30, 45, 366, 58, 30) == 'MERRYCHRISTMAS'
