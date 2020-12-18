"""
Function implementations of Huffman code algorithms from
MATH3411 Chapter 3 Compression Coding
"""

from fractions import Fraction
from math import isclose


def calculate_huffman_avg_len(radix, probabilities, *args, **kwargs):
    if not isclose(sum(probabilities), 1):
        probabilities = list(map(str, probabilities))
        raise ValueError(f"Probabilities {probabilities} do not sum to 1")

    # add dummy probabilities
    if radix > 2:
        while len(probabilities) % (radix - 1) != 1:
            probabilities.append(Fraction(0))

    avg_len = []
    while len(probabilities) > 1:
        probabilities.sort()
        new_probability = sum(probabilities[:radix])
        probabilities = probabilities[radix:] + [new_probability]
        avg_len.append(new_probability)

    return sum(avg_len)


class Node:
    def __init__(self, probability, source_no=0):
        self.probability = probability
        self.value = None
        self.source_no = source_no
        self.parents = []

    def __lt__(self, other):
        if self.probability == other.probability:
            return self.source_no > other.source_no
        return self.probability < other.probability

    def __add__(self, other):
        if isinstance(other, int):
            return Node(self.probability + other)
        return Node(self.probability + other.probability)

    def __radd__(self, other):
        return self.__add__(other)

    def __str__(self):
        return (
            f"p={self.probability}, "
            f"value={self.value}, "
            f"is_source={self.source_no}, "
            f"parents={self.parents}"
        )

    def __repr__(self):
        return self.__str__()


def evaluate_nodes(node, child_code, source_values):
    if node.value is not None:
        child_code += node.value

    if node.parents:
        for parent in node.parents:
            evaluate_nodes(parent, child_code, source_values)
    else:
        source_values.append((node.source_no, node.probability, child_code))


def generate_huffman(radix, probabilities):
    if not isclose(sum(probabilities), 1):
        probabilities = list(map(str, probabilities))
        raise ValueError(f"Probabilities {probabilities} do not sum to 1")
    no_symbols = len(probabilities)

    # add dummy probabilities
    if radix > 2:
        while len(probabilities) % (radix - 1) != 1:
            probabilities.append(Fraction(0))

    nodes = [Node(p, i) for i, p in enumerate(probabilities, 1)]
    nodes.sort()
    while len(nodes) > 0:
        new_node = sum(nodes[:radix])

        for index, node in enumerate(reversed(nodes[:radix])):
            node.value = str(index)
            new_node.parents.append(node)
        nodes = nodes[radix:]

        if len(nodes) == 0:
            root = new_node
            break

        for index, node in enumerate(nodes):
            if new_node < node:
                nodes = nodes[:index] + [new_node] + nodes[index:]
                break
            elif index == len(nodes) - 1:
                nodes.append(new_node)
                break

    codes = []
    evaluate_nodes(root, "", codes)
    codes.sort()
    return codes[:no_symbols]
