from math import floor

from src.exceptions import IccshValueError


def calculate_gcd(a, b, *args, **kwargs):
    if a == 0 or b == 0:
        return None, []

    if max(a, b) == b:
        a, b = b, a

    eqns = []
    gcd = -1
    while True:
        q = floor(a / b)
        r = a % b
        eqns.append((a, b, q, r))
        a, b = b, r
        if r == 0:
            gcd = a
            break

    return gcd, eqns


def solve_bezout_identity(d, a, b, *args, **kwargs):
    gcd, eqns = calculate_gcd(a, b)
    if gcd != d:
        raise IccshValueError(f"{d} != gcd({a}, {b})")

    eqns.pop()  # remove final eqn with remainder 0
    # initialise bezout's identity equation
    init = eqns.pop()
    bezout = [init[0], 1, init[1], -1 * init[2]]
    for eqn in reversed(eqns):
        bezout[0], bezout[1], bezout[2], bezout[3] = (
            eqn[0],
            bezout[3],
            bezout[0],
            bezout[1] + bezout[3] * -1 * eqn[2],
        )

    x, y = bezout[1], bezout[3]
    if max(a, b) == b:
        x, y = y, x
    print(f"{d} = {a}*{x} + {b}*{y}")
    return x, y


def get_modular_units(m):
    def is_unit(a, m):
        gcd, _ = calculate_gcd(a, m)
        return gcd == 1

    return list(filter(lambda a: is_unit(a, m), range(m)))


def find_eulers_phi(m, *args, silent=False, **kwargs):
    units = get_modular_units(m)
    if not silent:
        print("{" + ", ".join(map(str, units)) + "}")
    return len(units)


def find_order(m, a, *args, **kwargs):
    for i in range(1, m):
        if a ** i % m == 1:
            return i

    return -1


def find_primitive_elements(n):
    units = get_modular_units(n)

    def is_primitive(a, n):
        return find_order(n, a) == len(units)

    return list(filter(lambda a: is_primitive(a, n), units))
