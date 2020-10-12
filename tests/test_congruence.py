from src.error_correction import eval_congruence


def test_congruence():
    assert eval_congruence(4, 7, b=2) == 4
    assert eval_congruence(5, 11, b=4) == 3
    assert eval_congruence(3, 5, b=0) == 0
    assert eval_congruence(2, 5, b=1) == 3
