from fractions import Fraction
from math import ceil, log


def eval_kraft_mcmillan(radix, *args, **kwargs):
    return sum(map(lambda l: Fraction(1, radix ** l), args))


def eval_kraft_mcmillan_length(k, radix, *args, **kwargs):
    curr_k = eval_kraft_mcmillan(radix, *args)
    length = int(log(k - curr_k) / log(1 / radix))
    return length


def eval_kraft_mcmillan_min_length(radix, *args, **kwargs):
    curr_k = eval_kraft_mcmillan(radix, *args)
    length = ceil(log(1 - curr_k) / log(1 / radix))
    return length


def eval_kraft_mcmillan_radix(*args, **kwargs):
    for i in range(2, 100):
        k = eval_kraft_mcmillan(i, *args)
        if k <= 1:
            return i
    return -1
