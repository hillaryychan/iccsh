from math import ceil, sqrt
from src.ch5.number_theory import calculate_gcd


def is_prime(n, *args, **kwargs):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    return True


def is_pseudo_prime(n, a, *args, **kwargs):
    gcd, _ = calculate_gcd(n, a)
    if gcd != 1:
        return False

    return a ** (n - 1) % n == 1


def generate_primes(n, *args, **kwargs):
    """
    Generate primes less than or equal to n
    """
    return list(filter(is_prime, range(2, n + 1)))


def is_prime_lucas_test(n, a, *args, **kwargs):
    if not is_prime(a):
        raise ValueError(f"{a} is not prime")
    gcd, _ = calculate_gcd(n, a)
    if gcd != 1:
        return False

    if a ** (n - 1) % n != 1:
        return False

    dividing_primes = list(
        filter(lambda p: (n - 1) % p == 0, generate_primes(n))
    )
    for prime in dividing_primes:
        if a ** ((n - 1) / prime) % n == 1:
            return False

    return True


def is_strong_pseudo_prime(n, a, *args, **kwargs):
    """
    Use the Miller-Rabin probabilistic primality test for given base a
    """
    # find s and t
    s, t = -1, -1
    for i in range(n):
        t = (n - 1) / 2 ** i
        if t % 2 == 1:
            s = i
            t = int(t)
            break
    if s == -1:
        raise ValueError(f"Could not find values s and t s.t {n} = 2^s*t + 1")

    if a ** t % n == 1:
        return True

    for r in range(s):
        power = (2 ** r) * t
        if a ** power % n == n - 1:
            return True

    return False


def fermat_factorise(n, *args, **kwargs):
    if n % 2 == 0:
        raise ValueError(f"{n} is not odd for Fermat factorisation")
    start = ceil(sqrt(n))
    a, b = 0, 0
    for t in range(start, n + 1):
        s = sqrt(t ** 2 - n)
        if s.is_integer():
            a = int(t + s)
            b = int(t - s)
            break
    return (a, b)
