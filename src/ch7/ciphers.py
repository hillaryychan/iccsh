def shift_letter(shift, letter):
    if not letter.isalpha():
        return letter

    start = ord('a')
    if (letter.isupper()):
        start = ord('A')
    return chr(start + ((ord(letter) - start + shift) % 26))


def shift_message(shift, message):
    return ''.join(map(lambda l: shift_letter(shift, l), message))


def shift_cipher(shift, *messages, **kwargs):
    shift %= 26
    return ' '.join(map(lambda msg: shift_message(shift, msg), messages))


def get_alpha_pos(letter):
    start = ord('a')
    if (letter.isupper()):
        start = ord('A')
    return ord(letter) - start


def vigenere_shift(shifts, pos_letter):
    pos, letter = pos_letter
    if pos == -1:
        return letter

    used_shift = shifts[pos % len(shifts)]
    return shift_letter(used_shift, letter)


def vigenere_enumerate(message):
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
    message = ' '.join(messages)
    shifts = list(map(get_alpha_pos, key))
    if decode:
        shifts = list(map(lambda s: -s, shifts))
    return ''.join(map(lambda x: vigenere_shift(shifts, x),
                       vigenere_enumerate(message)))
