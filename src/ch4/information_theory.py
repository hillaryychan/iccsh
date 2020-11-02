from math import log


def calculate_entropy(radix, probabilities, *args, **kwargs):
    return sum(map(lambda p: -p*log(p)/log(radix), probabilities))


def generate_shannon_fano_table(radix, probabilities, *args, **kwargs):
    pass


def calculate_shannon_fano_avg_len(radix, probabilities, *args, **kwargs):
    pass
