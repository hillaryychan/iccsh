from src.ch3.comma_code import comma_decode, comma_encode


def test_comma_encode():
    assert comma_encode(4, "s3s1s4s1s5") == "1100111001111"
    assert comma_encode(4, "s2s1s2s5s2") == "10010111110"


def test_comma_decode():
    assert comma_decode(4, "11011101111010") == "s3s4s5s1s2"
    assert comma_decode(4, "11010110111110") == "s3s2s3s5s2"
