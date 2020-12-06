from src.ch6.algebraic_coding import cyclotomic_set


def test_cyclotomic_set():
    expected = {
        1: [1, 5],
        2: [2, 10],
        3: [3, 15],
        4: [4, 20],
        6: [6],
        7: [7, 11],
        8: [8, 16],
        9: [9, 21],
        12: [12],
        13: [13, 17],
        14: [14, 22],
        18: [18],
        19: [19, 23]
    }
    assert cyclotomic_set(5, 2) == expected


def test_cyclotomic_set_with_specified_k():
    expected = {
        3: [3, 15, 75],
        5: [5, 25, 1]
    }
    assert cyclotomic_set(5, 3, 3, 5) == expected
