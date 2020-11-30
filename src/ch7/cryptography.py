from src.ch2.error_correction import eval_congruence
from src.ch5.number_theory import find_eulers_phi

RSA_STD_ENCODING = ['0', '1', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def rsa_exponent_key(n, e, *args, **kwargs):
    n_phi = find_eulers_phi(n, silent=True)
    return eval_congruence(e, n_phi, b=1, silent=True)
# rsa encode
# rsa decode
# unicity distance?
