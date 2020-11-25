import pytest
from src.ch5.primality_testing import (is_pseudo_prime,
                                       fermat_factorise)


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
