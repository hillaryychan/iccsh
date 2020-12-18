from src.ch3.dictionary_code import lz78_encode, lz78_decode


def test_lz78_encode():
    assert lz78_encode("bccbcbacbabcbac") == [
        ("b", (0, "b")),
        ("c", (0, "c")),
        ("cb", (2, "b")),
        ("cba", (3, "a")),
        ("cbab", (4, "b")),
        ("cbac", (4, "c")),
    ]

    assert lz78_encode("caaaabaaaaaab") == [
        ("c", (0, "c")),
        ("a", (0, "a")),
        ("aa", (2, "a")),
        ("ab", (2, "b")),
        ("aaa", (3, "a")),
        ("aaab", (5, "b")),
    ]


def test_lz78_decode():
    outputs = [(0, "c"), (1, "c"), (2, "b"), (3, "c"), (3, "b"), (4, "a")]
    assert lz78_decode(outputs) == "cccccbccbcccbbccbca"

    outputs = [(0, "b"), (1, "b"), (2, "c"), (3, "a"), (4, "b"), (5, "b")]
    assert lz78_decode(outputs) == "bbbbbcbbcabbcabbbcabb"
