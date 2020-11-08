from math import floor


def calculate_gcd(a, b, *args, **kwargs):
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
        raise ValueError(f"{d} != gcd({a}, {b})")

    eqns.pop()  # remove final eqn with remainder 0
    # initialise bezout's identity equation
    init = eqns.pop()
    bezout = [init[0], 1, init[1], -1*init[2]]
    for eqn in reversed(eqns):
        bezout[0], bezout[1], bezout[2], bezout[3] = eqn[0], bezout[3], bezout[0], bezout[1] + bezout[3]*-1*eqn[2]  # noqa: E501

    x, y = bezout[1], bezout[3]
    if max(a, b) == b:
        x, y = y, x
    print(f"{d} = {a}*{x} + {b}*{y}")
    return x, y


def find_eulers_phi(m):
    def is_unit(a, m):
        gcd, _ = calculate_gcd(a, m)
        return gcd == 1

    units = list(filter(lambda a: is_unit(a, m), range(1, m)))
    print('{' + ', '.join(map(str, units)) + '}')
    return len(units)
