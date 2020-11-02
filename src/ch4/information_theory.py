from math import log, ceil


def calculate_entropy(radix, probabilities, *args, **kwargs):
    return sum(map(lambda p: -p*log(p)/log(radix), probabilities))


def shannon_fano_table(radix, probabilities, *args, **kwargs):
    def create_record(p):
        return (p, 1/p, ceil(log(1/p)/log(radix)))
    return list(map(create_record, probabilities))


def calculate_shannon_fano_avg_len(radix, probabilities, *args, **kwargs):
    pass
