from src.ch2.error_correction import eval_congruence
from src.ch5.number_theory import find_eulers_phi

RSA_STD_ENCODING = ['0', '1', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def rsa_exponent_key(n, e, *args, **kwargs):
    n_phi = find_eulers_phi(n, silent=True)
    return eval_congruence(e, n_phi, b=1, silent=True)


def rsa_encrypt(n, e, message, *args, **kwargs):
    message = message.upper()

    def encrypt(letter):
        return str(RSA_STD_ENCODING.index(letter)**e % n)

    return ' '.join(map(encrypt, message))


def rsa_decrypt(n, d, *codes, **kwargs):
    def decrypt(letter):
        return RSA_STD_ENCODING[letter**d % n]

    return ''.join(map(decrypt, codes))
