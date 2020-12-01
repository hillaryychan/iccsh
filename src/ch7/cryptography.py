from itertools import product

from src.ch2.error_correction import eval_congruence
from src.ch5.number_theory import find_eulers_phi

RSA_STD_ENCODING = ['0', '1', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def rsa_exponent_key(n, e, *args, **kwargs):
    n_phi = find_eulers_phi(n, silent=True)
    return eval_congruence(e, n_phi, b=1, silent=True)


def _rsa_encrypt(n, e, message, *args, **kwargs):
    message = message.upper()
    return list(map(lambda char: RSA_STD_ENCODING.index(char)**e % n, message))


def _rsa_decrypt(n, d, *codes, **kwargs):
    return ''.join(map(lambda code: RSA_STD_ENCODING[code**d % n], codes))


def rsa_encrypt_scheme(scheme, n, e, message, *args, **kwargs):
    message = message.upper()
    if scheme == 1:
        return _rsa_encrypt(n, e, message, *args, **kwargs)

    encrypted = []
    indexes = list(map(lambda l: RSA_STD_ENCODING.index(l), message))
    while len(indexes) > 0:
        items = indexes[:scheme]
        if len(items) != scheme:
            items.extend([RSA_STD_ENCODING.index(' ')] * (scheme-len(items)))

        value = sum(map(lambda pair: 29**pair[0]*pair[1],
                        enumerate(items[::-1])))
        encrypted.append(value**e % n)
        indexes = indexes[scheme:]

    return encrypted


def rsa_decrypt_scheme(scheme, n, d, *codes, **kwargs):
    if scheme == 1:
        return _rsa_decrypt(n, d, *codes)

    decrypted = map(lambda x: x**d % n, codes)

    def decode(value):
        def equals_value(combination):
            return sum(map(lambda pair: 29**pair[0]*pair[1],
                       enumerate(combination[::-1]))) == value

        combinations = product(list(range(29)), repeat=scheme)
        return next((x for x in combinations if equals_value(x)), None)

    msg = ''
    for value in decrypted:
        decoded_values = decode(value)
        if decoded_values is not None:
            msg += ''.join(map(lambda x: RSA_STD_ENCODING[x], decoded_values))

    return msg
