'''
Function implementations of arithmetic code from
MATH3411 Chapter 3 Compression Coding
'''

from math import isclose
from numpy import cumsum


def validate_arithmetic_symbols(source, probabilities):
    if len(source) != len(probabilities):
        raise ValueError(("No. of symbols and probabilities do not match\n"
                          f"source: {source}\n"
                          f"probabilities: {probabilities}"))
    if not isclose(sum(probabilities), 1):
        raise ValueError(f"Probabilities {probabilities} do not sum to 1")


def arithmetic_encode(source, probabilities, message, *args, **kwargs):
    validate_arithmetic_symbols(source, probabilities)
    message_symbols = set(message)
    if not (all(symbol in source for symbol in message_symbols)):
        raise ValueError((f"Message '{message}' contains symbol(s) not in "
                          f"source symbols {source}"))

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


def generate_intervals(probabilities):
    ends = cumsum(probabilities)
    intervals = []
    for index, end in enumerate(ends):
        intervals.append((sum(probabilities[:index]), end))
    return intervals


def find_interval(value, intervals):
    '''
    Find the interval in which value exists in.
    Returns the index where the interval interval_ends.
    '''
    for index, interval in enumerate(intervals):
        if interval[0] <= value <= interval[1]:
            return index
    return -1


def arithmetic_decode(source, probabilities, value, *args, **kwargs):
    validate_arithmetic_symbols(source, probabilities)
    intervals = generate_intervals(probabilities)

    message = ""
    index = find_interval(value, intervals)
    while index != (len(source) - 1) and index != -1:
        message += source[index]
        # scale value with value = (value - start) / interval width
        value = (value - sum(probabilities[:index]))/probabilities[index]
        index = find_interval(value, intervals)

    return message + source[-1]
