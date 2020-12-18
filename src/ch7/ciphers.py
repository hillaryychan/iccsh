from collections import Counter
from fractions import Fraction


def shift_letter(shift, letter):
    if not letter.isalpha():
        return letter

    start = ord("a")
    if letter.isupper():
        start = ord("A")
    return chr(start + ((ord(letter) - start + shift) % 26))


def shift_message(shift, message):
    return "".join(map(lambda l: shift_letter(shift, l), message))


def shift_cipher(shift, *messages, **kwargs):
    shift %= 26
    return " ".join(map(lambda msg: shift_message(shift, msg), messages))


def get_alpha_pos(letter):
    if not letter.isalpha():
        raise ValueError(f"get_alpha_pos: {letter} is not an alphabetical char")

    start = ord("a")
    if letter.isupper():
        start = ord("A")
    return ord(letter) - start


def vigenere_shift(shifts, pos_letter):
    pos, letter = pos_letter
    if pos == -1:
        return letter

    used_shift = shifts[pos % len(shifts)]
    return shift_letter(used_shift, letter)


def alpha_enumerate(message):
    """
    Enumerate only alphabetical chars
    """
    enumerated = []
    num = 0
    for c in message:
        if c.isalpha():
            enumerated.append((num, c))
            num += 1
        else:
            enumerated.append((-1, c))
    return enumerated


def vigenere_cipher(key, *messages, decode=False, **kwargs):
    message = " ".join(messages)
    shifts = list(map(get_alpha_pos, key))
    if decode:
        shifts = list(map(lambda s: -s, shifts))
    return "".join(
        map(lambda x: vigenere_shift(shifts, x), alpha_enumerate(message))
    )


def plaintext_feedback_encode(key, *messages, **kwargs):
    msg_key = filter(lambda c: c.isalpha(), key + "".join(messages))
    return vigenere_cipher(msg_key, *messages)


def plaintext_feedback_decode(key, *messages, **kwargs):
    message = " ".join(messages)
    shifts = list(map(lambda x: -get_alpha_pos(x), key))
    decoded = ""
    for pos, c in alpha_enumerate(message):
        if c.isalpha():
            letter = shift_letter(shifts[pos], c)
            decoded += letter
            shifts.append(-get_alpha_pos(letter))
        else:
            decoded += c
    return decoded


def ciphertext_feedback_encode(key, *messages, **kwargs):
    message = " ".join(messages)
    shifts = list(map(lambda x: get_alpha_pos(x), key))
    encoded = ""
    for pos, c in alpha_enumerate(message):
        if c.isalpha():
            letter = shift_letter(shifts[pos], c)
            encoded += letter
            shifts.append(get_alpha_pos(letter))
        else:
            encoded += c
    return encoded


def ciphertext_feedback_decode(key, *messages, **kwargs):
    msg_key = filter(lambda c: c.isalpha(), key + "".join(messages))
    return vigenere_cipher(msg_key, *messages, decode=True)


def index_of_coincidence(*messages, **kwargs):
    messages = map(lambda m: m.upper(), messages)
    message = "".join(messages)
    message = "".join(filter(lambda c: c.isalpha(), message))
    n = len(message)
    freq = Counter(message).values()
    return Fraction(sum(map(lambda f: f * f, freq)) - n) / (n * n - n)


def estimate_key_len(*messages, **kwargs):
    messages = map(lambda m: m.upper(), messages)
    message = "".join(messages)
    message = "".join(filter(lambda c: c.isalpha(), message))
    msg_len = len(message)
    ioc = index_of_coincidence(message)
    return (0.0273 * msg_len) / (
        (msg_len - 1) * ioc - 0.0385 * msg_len + 0.0658
    )
