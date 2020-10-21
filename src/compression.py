'''
Function implementations of algorithms from
MATH3411 Chapter 3 Compression Coding
'''

from fractions import Fraction
from math import log, ceil, isclose
from numpy import cumsum


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


def check_comma_message_symbols(length, message):
    gt_length = list(filter(lambda s: int(s) > (length + 1), message))
    if gt_length:
        raise ValueError((f"message '{message}' contains symbols which can be "
                          f"encoded by a comma code of length {length}"))


def generate_comma_code(length):
    code = []
    for i in range(length+1):
        if i == 0:
            code.append('0')
        elif i == length:
            code.append('1'*i)
        else:
            code.append('1'*i+'0')
    return code


def comma_encode(length, message, *args, **kwargs):
    message = list(filter(lambda s: s, message.split('s')))
    check_comma_message_symbols(length, message)
    code = generate_comma_code(length)
    encoded = ''
    for s in message:
        index = int(s) - 1
        encoded += code[index]
    return encoded


def find_comma_prefix(message, code):
    for c in code[::-1]:
        if message.startswith(c):
            return code.index(c)
    return -1


def comma_decode(length, message, *args, **kwargs):
    code = generate_comma_code(length)
    decoded = ''
    while len(message) > 0:
        prefix = find_comma_prefix(message, code)
        message = message[len(code[prefix]):]
        decoded += f"s{prefix+1}"
    return decoded


def find_prefix_entry(message, dictionary):
    '''
    Find the longest entry in dictionary which is a prefix of the given message
    '''
    for entry in dictionary[::-1]:
        if message.startswith(entry[0]):
            return dictionary.index(entry)
    return -1


def lz78_encode(message, *args, **kwargs):
    dictionary = []
    while len(message) > 0:
        prefix_entry = find_prefix_entry(message, dictionary)
        if prefix_entry == -1:
            next_char = message[0]
            entry = (next_char, (0, next_char))
            message = message[1:]
        else:
            prefix = dictionary[prefix_entry][0]
            next_char = message[len(prefix)]
            value = prefix + next_char
            entry = (value, (prefix_entry + 1, next_char))
            message = message[len(value):]
        dictionary.append(entry)
    return dictionary


def lz78_decode(outputs, *args, **kwargs):
    dictionary = []
    message = ''
    for i, c in outputs:
        if i == 0:
            suffix = c
            dictionary.append((c, (i, c)))
        else:
            entry = dictionary[i-1]
            suffix = entry[0]+c
            dictionary.append((entry[0]+c, (i, c)))
        message += suffix
    return message


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


def calculate_huffman_avg_len(radix, probabilities, *args, **kwargs):
    if not isclose(sum(probabilities), 1):
        probabilities = list(map(str, probabilities))
        raise ValueError(f"Probabilities {probabilities} do not sum to 1")

    # add dummy probabilities
    while len(probabilities) % (radix - 1) != 1:
        probabilities.append(Fraction(0))

    avg_len = []
    while len(probabilities) > 1:
        probabilities.sort()
        new_probability = sum(probabilities[:radix])
        probabilities = probabilities[radix:] + [new_probability]
        avg_len.append(new_probability)

    return sum(avg_len)
