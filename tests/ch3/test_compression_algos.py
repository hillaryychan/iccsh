from src.compression import (arithmetic_encode)
from numpy.testing import assert_almost_equal


def test_arithmetic_encode():
    result = arithmetic_encode(['a', 'b', '.'], [0.6, 0.2, 0.2], "baa.")
    assert_almost_equal(result, 0.6648)

    result = arithmetic_encode(['a', 'b', '.'], [0.4, 0.3, 0.3], "baa.")
    assert_almost_equal(result, 0.4408)
