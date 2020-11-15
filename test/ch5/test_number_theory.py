import pytest
from src.ch5.number_theory import (calculate_gcd,
                                   solve_bezout_identity,
                                   find_eulers_phi,
                                   find_order,
                                   find_primitive_elements,
                                   is_pseudo_prime,
                                   fermat_factorise)


def test_calculate_gcd():
    result, _ = calculate_gcd(324, 3876)
    assert result == 12

    result, _ = calculate_gcd(7412, 1513)
    assert result == 17

    result, _ = calculate_gcd(1024, 2187)
    assert result == 1


def test_calculate_gcd_with_zero():
    assert calculate_gcd(324, 0) == (None, [])
    assert calculate_gcd(0, 1513) == (None, [])
    assert calculate_gcd(0, 0) == (None, [])


def test_solve_bezout_identity():
    assert solve_bezout_identity(12, 324, 3876) == (12, -1)
    assert solve_bezout_identity(17, 7412, 1513) == (-10, 49)
    assert solve_bezout_identity(1, 1024, 2187) == (472, -221)


def test_find_eulers_phi():
    assert find_eulers_phi(24) == 8
    assert find_eulers_phi(36) == 12
    assert find_eulers_phi(17) == 16


def test_find_order():
    assert find_order(17, 7) == 16
    assert find_order(12, 5) == 2
    assert find_order(7, 3) == 6


def test_find_primitive_elements():
    assert find_primitive_elements(22) == [7, 13, 17, 19]
    assert find_primitive_elements(12) == []
    assert find_primitive_elements(7) == [3, 5]


def test_is_pseudo_prime():
    assert is_pseudo_prime(15, 2) is False
    assert is_pseudo_prime(15, 4) is True

    assert is_pseudo_prime(121, 5) is False
    assert is_pseudo_prime(121, 3) is True


def test_fermat_factorise():
    assert fermat_factorise(81719) == (323, 253)
    assert fermat_factorise(35581) == (221, 161)
    assert fermat_factorise(29029) == (203, 143)


def test_fermat_factorise_with_even_integer():
    with pytest.raises(ValueError) as exc:
        fermat_factorise(6)
    assert str(exc.value) == "6 is not odd for Fermat factorisation"
