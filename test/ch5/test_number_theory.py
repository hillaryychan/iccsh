from src.ch5.number_theory import (calculate_gcd,
                                   solve_bezout_identity,
                                   find_eulers_phi)


def test_calculate_gcd():
    result, _ = calculate_gcd(324, 3876)
    assert result == 12

    result, _ = calculate_gcd(7412, 1513)
    assert result == 17

    result, _ = calculate_gcd(1024, 2187)
    assert result == 1


def test_solve_bezout_identity():
    assert solve_bezout_identity(12, 324, 3876) == (12, -1)
    assert solve_bezout_identity(17, 7412, 1513) == (-10, 49)
    assert solve_bezout_identity(1, 1024, 2187) == (472, -221)


def test_eulers_phi():
    assert find_eulers_phi(24) == 8
    assert find_eulers_phi(36) == 12
    assert find_eulers_phi(17) == 16
