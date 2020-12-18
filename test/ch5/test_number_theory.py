from src.ch5.number_theory import (
    calculate_gcd,
    solve_bezout_identity,
    find_eulers_phi,
    find_order,
    find_primitive_elements,
)


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
