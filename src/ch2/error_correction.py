def get_isbn_digits(number):
    number = list(filter(lambda x: x.isdigit() or x == "X", number))
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
    digits = get_isbn_digits(number)
    if len(digits) != 10:
        raise ValueError(f"'{number}' is not an ISBN-10 number")
    pos = int(pos)
    if not 1 <= pos <= 10:
        raise ValueError(f"Can't have error in position {pos}")

    val = 0
    for i, num in enumerate(digits, 1):
        if i != pos:
            val += i * num

    correct_digit = -1
    for i in range(11):
        if (val + i * pos) % 11 == 0:
            correct_digit = i if i != 10 else "X"
            break

    return correct_digit


def get_weight(codewords, *args, **kwargs):
    weights = []
    for codeword in codewords:
        digits = list(filter(lambda x: x.isdigit() and x != "0", codeword))
        weights.append(len(digits))
    return weights


def get_distance(codeword1, codeword2, *args, **kwargs):
    return sum(a != b for a, b in zip(codeword1, codeword2))


def eval_congruence(a, m, *args, b=None, silent=False, **kwargs):
    for i in range(m):
        congruence = (a * i) % m
        if b is not None:
            if congruence == b:
                if not silent:
                    print(f"{a}*{i} ≡ {congruence} (mod {m})")
                return i
        else:
            if not silent:
                print(f"{a}*{i} ≡ {congruence} (mod {m})")
    return None


def add_codewords(radix, *args, **kwargs):
    radix = int(radix)
    all_digits = [map(int, codeword) for codeword in args]
    sum_digits = map(sum, zip(*all_digits))
    sum_digits = list(map(lambda x: str(x % radix), sum_digits))

    for codeword in args:
        print(codeword)
    print("-" * len(sum_digits))

    return "".join(sum_digits)
