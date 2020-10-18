'''
Function implementations of algorithms from
MATH3411 Chapter 3 Compression Coding
'''

from fractions import Fraction
from math import log, ceil


def eval_kraft_mcmillan(radix, *args, **kwargs):
    return sum(map(lambda l: Fraction(1, radix**l), args))


def eval_kraft_mcmillan_length(k, radix, *args, **kwargs):
    curr_k = eval_kraft_mcmillan(radix, *args)
    length = int(log(k - curr_k)/log(1/radix))
    return length


def eval_kraft_mcmillan_min_length(radix, *args, **kwargs):
    curr_k = eval_kraft_mcmillan(radix, *args)
    length = ceil(log(1 - curr_k)/log(1/radix))
    return length


def eval_kraft_mcmillan_radix(*args, **kwargs):
    for i in range(2, 100):
        k = sum(map(lambda l: Fraction(1, i**l), args))
        if k <= 1:
            return i
    return -1


def lz78_encode():
    pass


def lz78_decode():
    pass


def arithmetic_encode(source, probabilities, message):
    if len(source) != len(probabilities):
        raise ValueError(("No. of symbols and probabilities do not match\n"
                          f"source: {source}\n"
                          f"probabilities: {probabilities}"))
    message_symbols = set(message)
    if not (all(symbol in source for symbol in message_symbols)):
        raise ValueError((f"Message {message} contains symbol(s) not in source "
                          f"symbols {source}"))
    if sum(probabilities) != 1:
        raise ValueError(f"probabilities {probabilities} do not sum to 1")

    print("symbol: {:>10} {:>10}".format("start", "width"))
    start = 0
    width = 1
    for symbol in message:
        index = source.index(symbol)
        start = start + sum(probabilities[:index])*width
        width *= probabilities[index]
        print(f"{symbol:>6}: {start:10.5f} {width:10.5f}")
    end = start + width
    print(f"interval is [{start:.5f}, {end:.5f})")
    return (start + end)/2


def arithmetic_decode():
    pass
