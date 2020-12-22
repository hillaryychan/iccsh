import pytest

from src.ch5.primality_testing import (
    fermat_factorise,
    generate_primes,
    is_prime,
    is_prime_lucas_test,
    is_pseudo_prime,
)
from src.exceptions import IccshValueError


def test_is_prime():
    assert is_prime(97) is True
    assert is_prime(98) is False


def test_is_pseudo_prime():
    assert is_pseudo_prime(15, 2) is False
    assert is_pseudo_prime(15, 4) is True

    assert is_pseudo_prime(121, 5) is False
    assert is_pseudo_prime(121, 3) is True


def test_generate_primes():
    assert generate_primes(20) == [2, 3, 5, 7, 11, 13, 17, 19]
    assert generate_primes(19) == [2, 3, 5, 7, 11, 13, 17, 19]


def test_is_prime_lucas_test():
    assert is_prime_lucas_test(257, 3) is True
    assert is_prime_lucas_test(257, 2) is False


def test_fermat_factorise():
    assert fermat_factorise(81719) == (323, 253)
    assert fermat_factorise(35581) == (221, 161)
    assert fermat_factorise(29029) == (203, 143)


def test_fermat_factorise_with_even_integer():
    with pytest.raises(IccshValueError) as exc:
        fermat_factorise(6)
    assert str(exc.value) == "6 is not odd for Fermat factorisation"
