'''
Function implementations of algorithms from MATH3411
'''


def get_isbn_digits(number):
    number = list(filter(lambda x: x.isdigit() or x == 'X', number))
    return list(map(lambda x: int(x) if x.isdigit() else 10, number))


def is_isbn(number, *args, **kwargs):
    number = get_isbn_digits(number)
    # Must have 10 digits
    if len(number) != 10:
        return False

    val = 0
    for i, num in enumerate(number, 1):
        val += i * num

    return val % 11 == 0


def isbn_fix(number, pos, *args, **kwargs):
    number = get_isbn_digits(number)
    if len(number) != 10:
        raise ValueError("Not an ISBN-10 number")
    pos = int(pos)

    val = 0
    for i, num in enumerate(number, 1):
        if i != pos:
            val += i * num

    correct_digit = -1
    for i in range(11):
        if (val + i * pos) % 11 == 0:
            correct_digit = i if i != 10 else 'X'
            break

    return correct_digit


def get_weight(codewords, *args, **kwargs):
    weights = []
    for codeword in codewords:
        digits = list(filter(lambda x: x.isdigit() and x != '0', codeword))
        weights.append(len(digits))
    return weights


def get_distance(codeword1, codeword2, *args, **kwargs):
    return sum(a != b for a, b in zip(codeword1, codeword2))
