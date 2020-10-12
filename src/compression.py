'''
Function implementations of algorithms from
MATH3411 Chapter 3 Compression Coding
'''

from fractions import Fraction


def eval_kraft_mcmillan(radix, *args, **kwargs):
    return sum(map(lambda l: Fraction(1, radix**l), args))
