from src.ch5.number_theory import (calculate_gcd,
                                   solve_bezout_identity)


def test_calculate_gcd():
    calculate_gcd(324, 3876) == 12
    calculate_gcd(7412, 1513) == 17
    calculate_gcd(1024, 2187) == 1


def test_solve_bezout_identity():
    solve_bezout_identity(12, 324, 3876) == 12, -1
    solve_bezout_identity(17, 7412, 1513) == -10, 49
    solve_bezout_identity(1, 1024, 2187) == 472, -221
