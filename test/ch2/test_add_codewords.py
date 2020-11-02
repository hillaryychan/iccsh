from src.ch2.error_correction import add_codewords


def test_addd_codeword_with_no_codewords():
    assert add_codewords('1') == ''
    assert add_codewords('6') == ''
    assert add_codewords('8') == ''


def test_add_codeword_with_one_codeword():
    assert add_codewords('2', '11110') == '11110'
    assert add_codewords('3', '011102') == '011102'
    assert add_codewords('4', '1213') == '1213'


def test_add_codewords_with_two_codewords():
    assert add_codewords('2', '01001', '11110') == '10111'
    assert add_codewords('3', '110001', '011102') == '121100'
    assert add_codewords('7', '0451', '1044') == '1425'


def test_add_codewords_with_multiple_codewords():
    assert add_codewords('2', '10111110', '11010110',
                         '11100010', '01110010', '01111000') == '10000000'
    assert add_codewords('3', '211021', '202202', '211010') == '021200'
    assert add_codewords('5', '0314', '2320', '0333', '1304') == '3211'
