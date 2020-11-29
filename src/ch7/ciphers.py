def shift_letter(shift, letter):
    start = ord('a')
    if (letter.isupper()):
        start = ord('A')
    return chr(start + ((ord(letter) - start + shift) % 26))


def shift_message(shift, message):
    return ''.join(map(lambda l: shift_letter(shift, l), message))


def shift_encode(shift, *messages, **kwargs):
    shift %= 26
    return ' '.join(map(lambda msg: shift_message(shift, msg), messages))
