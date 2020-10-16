'''
Function implementations of algorithms from
MATH3411 Chapter 3 Compression Coding
'''

from fractions import Fraction
from math import log


def eval_kraft_mcmillan(radix, *args, **kwargs):
    return sum(map(lambda l: Fraction(1, radix**l), args))


def eval_kraft_mcmillan_length(k, radix, *args, **kwargs):
    curr_k = eval_kraft_mcmillan(radix, *args)
    length = int(log(k - curr_k)/log(1/radix))
    return length


def eval_kraft_mcmillan_radix(*args, **kwargs):
    for i in range(2, 100):
        k = sum(map(lambda l: Fraction(1, i**l), args))
        if k <= 1:
            return i
    return -1
