def is_isbn(number, *args, **kwargs):
    number = get_isbn_digits(number)
    # Must have 10 digits
    if len(number) != 10:
        return False

    val = 0
    for i, num in enumerate(number, 1):
        val += i * num

    return val % 11 == 0

def is_isbn(number, *args, **kwargs):
    number = get_isbn_digits(number)
    # Must have 10 digits
    if len(number) != 10:
        return False

    val = 0
    for i, num in enumerate(number, 1):
        val += i * num

    return val % 11 == 0

def is_isbn(number, *args, **kwargs):
    number = get_isbn_digits(number)
    # Must have 10 digits
    if len(number) != 10:
        return False

    val = 0
    for i, num in enumerate(number, 1):
        val += i * num

    return val % 11 == 0
