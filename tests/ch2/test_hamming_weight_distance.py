from src.ch2.error_correction import get_weight, get_distance


def test_get_weight_with_zero_codeword():
    assert get_weight(['000000']) == [0]


def test_get_weight_with_non_zero_codeword():
    assert get_weight(['222010110020220']) == [9]
    assert get_weight(['110100']) == [3]


def test_get_weight_with_multiple_codewords():
    codewords = ['00011010', '10100001', '11111100']
    assert get_weight(codewords) == [3, 3, 6]

    codewords = ['0110120', '0020210', '11211001',
                 '1110000', '2102102', '0001110']
    assert get_weight(codewords) == [4, 3, 6, 3, 5, 3]


def test_get_distance_with_same_codewords():
    assert get_distance('001001110', '001001110') == 0
    assert get_distance('2022120001200', '2022120001200') == 0
    assert get_distance('00000000', '00000000') == 0


def test_get_distance_with_diff_codewords():
    assert get_distance('10001001', '10100101') == 3
    assert get_distance('2022220001100', '0000000000000') == 7
    assert get_distance('4402', '3620') == 4
