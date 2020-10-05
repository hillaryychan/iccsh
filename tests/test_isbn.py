import pytest
from src.utils import is_isbn, isbn_fix


def test_is_isbn_with_valid_isbn():
    assert is_isbn('0-387-97993-X') is True
    assert is_isbn('038797993X') is True


def test_is_isbn_with_invalid_isbn():
    assert is_isbn('0-387-97993-9') is False
    assert is_isbn('0387979939') is False
    assert is_isbn('I am a string') is False
    assert is_isbn('123456789') is False


def test_isbn_fix():
    assert isbn_fix('0-245-59812-2', 10) == 'X'
    assert isbn_fix('0245598122', 10) == 'X'

    assert isbn_fix('4-019-78703-3', 4) == 6
    assert isbn_fix('4019787033', 4) == 6


def test_isbn_fix_with_non_isbn():
    with pytest.raises(ValueError) as exc:
        isbn_fix('I am not an ISBN', 1)
    assert str(exc.value) == "'I am not an ISBN' is not an ISBN-10 number"

    with pytest.raises(ValueError) as exc:
        isbn_fix('12345', 1)
    assert str(exc.value) == "'12345' is not an ISBN-10 number"

    with pytest.raises(ValueError) as exc:
        isbn_fix('01234567890', 1)
    assert str(exc.value) == "'01234567890' is not an ISBN-10 number"


def test_isbn_fix_with_invalid_pos():
    with pytest.raises(ValueError) as exc:
        isbn_fix('5-666-15994-2', 0)
    assert str(exc.value) == "Can't have error in position 0"

    with pytest.raises(ValueError) as exc:
        isbn_fix('5-666-15994-2', 11)
    assert str(exc.value) == "Can't have error in position 11"
