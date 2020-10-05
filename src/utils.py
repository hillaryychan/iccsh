'''
Function implementations of algorithms from MATH3411
'''


def gcd(x, y, *args, **kwargs):
    '''
    The greatest common divisor (gcd) of x and y
    '''
    pass


def lcm(x, y, *args, **kwargs):
    '''
    The lowest common multiple (lcm) of x and y
    '''
    pass


def mod(a, n, *args, **kwargs):
    '''
    The modulo operation. Returns the remainder of a division.
    '''
    print(f"{a} mod {n} = {a % n}")


def mod_congruent(a, n, *args, **kwargs):
    '''
    The congruence relation between positve integer n, and two integers a and b
    such that a ≡ b (mod n)
    '''
    print(f"{a} ≡ {a % n} (mod {n})")
    pass


def mod_inverse(a, n, *args, **kwargs):
    '''
    The modular multiplicative inverse of an integer a is an integer x such that
    the product ax is congruent to 1 with respect to the modulus n.
    This can be written as ax ≡ 1 (mod n)
    '''
    pass


def get_isbn_digits(number):
    number = list(filter(lambda x: int(x.isdigit()) or x == 'X', number))
    return list(map(lambda x: int(x) if x.isdigit() else 10, number))


def is_isbn(number, *args, **kwargs):
    '''
    Checks the ISBN-10 number is correct.
    '''
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
        print("Not an ISBN-10 number")
        return
    pos = int(pos)

    val = 0
    for i, num in enumerate(number, 1):
        if i != pos:
            val += i * num

    correct_digit = -1
    for i in range(11):
        if (val + i * pos) % 11 == 0:
            correct_digit = i
            break

    return correct_digit
