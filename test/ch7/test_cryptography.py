from src.ch7.cryptography import (
    rsa_decrypt_scheme,
    rsa_encrypt_scheme,
    rsa_exponent_key,
)


def test_rsa_exponent_key():
    assert rsa_exponent_key(10033, 1787) == 11
    assert rsa_exponent_key(10033, 11) == 1787
    assert rsa_exponent_key(551, 55) == 55


def test_rsa_encrypt_scheme():
    assert rsa_encrypt_scheme(1, 551, 55, "hi") == [409, 182]
    assert rsa_encrypt_scheme(2, 1147, 17, "HelLo") == [1037, 424, 991]


def test_rsa_decrypt_scheme():
    assert rsa_decrypt_scheme(1, 551, 55, 302, 241) == "OK"
    assert (
        rsa_decrypt_scheme(
            1,
            391,
            3,
            366,
            14,
            126,
            126,
            3,
            249,
            258,
            126,
            148,
            30,
            45,
            366,
            58,
            30,
        )
        == "MERRYCHRISTMAS"
    )
    assert rsa_decrypt_scheme(2, 1147, 953, 1037, 424, 991) == "HELLO "
    assert rsa_decrypt_scheme(3, 10033, 11, 8695) == "ARR"
