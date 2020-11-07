import cmd
import re

from ast import literal_eval
from colorama import Fore
from fractions import Fraction
from functools import wraps

from src.ch2 import error_correction
from src.ch3 import (kraft_mcmillan,
                     comma_code,
                     dictionary_code,
                     arithmetic_code,
                     huffman_code)
from src.ch4 import information_theory


def is_decimal(value):
    try:
        float(value)
        return True
    except Exception:
        return False


def do_help_on_error(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as exc:
            print(f"{Fore.RED}{type(exc).__name__}: {exc}{Fore.RESET}")
            self.do_help(func.__name__[3:])
    return wrapper


class ICCShell(cmd.Cmd):
    intro = ('Welcome to the MATH3411 Shell.\n'
             'Type "help" or "?" to list commands. '
             'Type "exit" or ctrl-d to exit.')
    prompt = f"{Fore.GREEN}> {Fore.RESET}"

    def do_exit(self, args):
        '''
        Exit MATH3411 shell.
        '''
        print()
        return True

    def do_EOF(self, args):
        '''
        Exit MATH3411 shell.
        '''
        return self.do_exit(args)

    # Ch2. Error Correction and Detection

    @do_help_on_error
    def do_is_isbn(self, args):
        '''
        Usage: is_isbn ISBN

        Check a number satisfies the ISBN-10 check condition.
        '''
        print(error_correction.is_isbn(*parse_args(args)))

    @do_help_on_error
    def do_isbn_fix(self, args):
        '''
        Usage: isbn_fix ISBN ERROR_DIGIT

        Correct the nth digit in a given ISBN-10 number.
        '''
        result = error_correction.isbn_fix(*parse_args(args))
        if result != -1:
            print(f"Correct digit is {result}")
        else:
            print("Could not find correct digit")

    @do_help_on_error
    def do_weight(self, args):
        '''
        Usage: weight CODEWORD

        Find the weight of given codewords. That is, the distance between a
        codeword and the zero-codeword, or the number of non-zero values in each
        codeword.
        '''
        codewords = parse_args(args)
        result = error_correction.get_weight(codewords)
        for codeword, weight in zip(codewords, result):
            print(f"Weight of {codeword} is {weight}")

    @do_help_on_error
    def do_distance(self, args):
        '''
        Usage: distance CODEWORD1 CODEWORD2

        Find the distance between two codewords. That is, the number of values
        that differ for each position in the codewords.
        '''
        result = error_correction.get_distance(*parse_args(args))
        print(f"Distance is {result}")

    @do_help_on_error
    def do_congruence(self, args):
        '''
        Usage: congruence a m [b]

        Evaluate linear congruences a*x ≡ b (mod m).  '''
        args = list(map(int, parse_args(args)))
        target = args.pop(2) if len(args) > 2 else None
        result = error_correction.eval_congruence(*args, b=target)
        if result is not None:
            print(f"x is {result}")

    @do_help_on_error
    def do_add_codewords(self, args):
        '''
        Usage: add_codewords RADIX CODEWORD1 CODEWORD2 [CODEWORDS...]

        Add codewords of a given radix together.
        '''
        result = error_correction.add_codewords(*parse_args(args))
        print(result)

    # Ch3. Compression Coding

    @do_help_on_error
    def do_kraft_mcmillan(self, args):
        '''
        Usage: kraft_mcmillan RADIX LENGTH [LENGTHS...]

        Evaluate Kraft-McMillan inequality
        '''
        args = list(map(int, parse_args(args)))
        result = kraft_mcmillan.eval_kraft_mcmillan(*args)
        print(f"K = {result} = {float(result)}")
        print(f"K ≤ 1 is {result <= 1}")

    @do_help_on_error
    def do_kraft_mcmillan_length(self, args):
        '''
        Usage: kraft_mcmillan_length K RADIX LENGTH [LENGTHS...]

        Find the missing codeword length that satisifes the Kraft-McMillan
        Theorem given the coefficient K, radix and other codeword lengths
        '''
        args = parse_args(args)
        k = Fraction(args[0])
        radix = int(args[1])
        lengths = [int(length) for length in args[2:]]
        result = kraft_mcmillan.eval_kraft_mcmillan_length(k, radix, *lengths)

        print(f"length is {result}")
        result_args = [str(x) for x in [radix] + lengths + [result]]
        self.do_kraft_mcmillan(' '.join(result_args))

    @do_help_on_error
    def do_kraft_mcmillan_min_length(self, args):
        '''
        Usage: kraft_mcmillan_min_length RADIX LENGTH [LENGTHS...]

        Find the minimum codeword length that satisifes the Kraft-McMillan
        Theorem given the radix and other codeword lengths
        '''
        args = list(map(int, parse_args(args)))
        result = kraft_mcmillan.eval_kraft_mcmillan_min_length(*args)

        print(f"length is {result}")
        result_args = [str(x) for x in args + [result]]
        self.do_kraft_mcmillan(' '.join(result_args))

    @do_help_on_error
    def do_kraft_mcmillan_radix(self, args):
        '''
        Usage: kraft_mcmillan_radix LENGTH [LENGTHS...]

        Find the minimum radix that satisifes the Kraft-McMillan Theorem given
        the codeowrd lengths
        '''
        args = list(map(int, parse_args(args)))
        result = kraft_mcmillan.eval_kraft_mcmillan_radix(*args)
        if result != -1:
            print(f"radix is {result}")
        else:
            print("length > 100")

    @do_help_on_error
    def do_comma_encode(self, args):
        '''
        Usage: comma_encode LENGTH MESSAGE

        Encode a message using a comma code of a given length
        Note: message is expected to be in format 's1s2s3s4'
        '''
        args = list(parse_args(args))
        length = int(args.pop(0))
        result = comma_code.comma_encode(length, *args)
        print(f"encoded message is '{result}'")

    @do_help_on_error
    def do_comma_decode(self, args):
        '''
        Usage: comma_decode LENGTH MESSAGE

        Decode a message encoded using a comma code of a given length
        '''
        args = list(parse_args(args))
        length = int(args.pop(0))
        result = comma_code.comma_decode(length, *args)
        print(f"decoded message is '{result}'")

    @do_help_on_error
    def do_lz78_encode(self, args):
        '''
        Usage: lz78_encode MESSAGE

        Encodes a message using the LZ78 algorithm.
        '''
        result = dictionary_code.lz78_encode(*parse_args(args))
        print("no. entry      output")
        for index, entry in enumerate(result):
            print(f"{index+1:<3d} {entry[0]:10} {entry[1]}")

    @do_help_on_error
    def do_lz78_decode(self, args):
        '''
        Usage: lz78_decode OUTPUT [OUTPUTS...]

        Decode a message encoded with the LZ78 algorithm.
        '''
        outputs = map(lambda s: re.sub(r"([a-zA-Z])", r"'\1'", s),
                      parse_args(args))
        outputs = list(map(literal_eval, outputs))
        result = dictionary_code.lz78_decode(outputs)
        print(f"message is '{result}'")

    @do_help_on_error
    def do_arithmetic_encode(self, args):
        '''
        Usage: arithmetic_encode SOURCE_SYMBOLS SOURCE_PROBABILITIES MESSAGE

        Encode a message using arithmetic encoding with the provided source
        symbols and their respective probabilities.
        Note: symbols must be 1 char long.
        Note: you can use anything as a stop symbol as long as YOU know it's
        the stop symbol.
        '''
        args = list(parse_args(args))

        source = list(args.pop(0))
        msg = args.pop()
        probabilities = list(map(float, args))
        result = arithmetic_code.arithmetic_encode(source, probabilities, msg)
        print(f"a valid value would be {result:.5f}")

    @do_help_on_error
    def do_arithmetic_decode(self, args):
        '''
        Usage: arithmetic_decode SOURCE_SYMBOLS SOURCE_PROBABILITIES VALUE

        Decode an arithmetic encoded message using the provided source symbols
        and their respsective probabilities.
        Note: symbols must be 1 char long.
        Note: you can use anything as a stop symbol as long as YOU know it's
        the stop symbol.
        '''
        args = list(parse_args(args))

        source = list(args.pop(0))
        probabilities = list(map(float, args))
        value = probabilities.pop()
        result = arithmetic_code.arithmetic_decode(source, probabilities, value)
        print(f"decoded message is {result}")

    @do_help_on_error
    def do_huffman_avg_len(self, args):
        '''
        Usage: huffman_avg_len RADIX PROBABILITY [PROBABILITIES...]

        Calculates the average length of a Huffman code of the given radix
        and probabilities.
        '''
        args = list(parse_args(args))
        radix = int(args.pop(0))
        probabilities = list(map(Fraction, args))
        result = huffman_code.calculate_huffman_avg_len(radix, probabilities)
        print(f"average length of code is {result}")

    @do_help_on_error
    def do_huffman_generate(self, args):
        '''
        Usage: huffman_generate RADIX PROBABILITY [PROBABILITIES...]

        Generate a Huffman code based on the given radix and probabilities of
        source symbols. The code is generate using the "place high strategy".
        '''
        args = list(parse_args(args))
        radix = int(args.pop(0))
        probabilities = list(map(Fraction, args))
        result = huffman_code.generate_huffman(radix, probabilities)

        decimal = all(is_decimal(x) for x in args)
        print("source probability code")
        for source, probability, code in result:
            probability = probability if not decimal else float(probability)
            print(f"s{source:<5} {str(probability):11} {code}")

    # Ch4. Information Theory

    @do_help_on_error
    def do_entropy(self, args):
        '''
        Usage: entropy RADIX PROBABILITY [PROBABILITIES...]

        Calculate the entropy for given probabilities and radix.
        '''
        args = list(parse_args(args))
        radix = int(args.pop(0))
        probabilities = list(map(Fraction, args))
        result = information_theory.calculate_entropy(radix, probabilities)
        print(f"entropy is {result}")

    @do_help_on_error
    def do_shannon_fano(self, args):
        '''
        Usage: entropy RADIX PROBABILITY [PROBABILITIES...]

        Generate a table indicating the lengths of symbols with provided
        probabilities if they were encoded using the Shannon-Fano code.
        '''
        args = list(parse_args(args))
        radix = int(args.pop(0))
        probabilities = list(map(Fraction, args))
        result = information_theory.shannon_fano_table(radix, probabilities)

        decimal = all(is_decimal(x) for x in args)
        print("p       1/p     SF_length")
        for p, inverse_p, length in result:
            if decimal:
                p = float(p)
                inverse_p = float(inverse_p)
                print(f"{p:<7.6} {inverse_p:<7.6} {length}")
            else:
                print(f"{str(p):7} {str(inverse_p):7} {length}")

    @do_help_on_error
    def do_shannon_fano_avg_len(self, args):
        '''
        Usage: entropy RADIX PROBABILITY [PROBABILITIES...]

        Given the radix and source probabilities, calculate the average length
        if a message encoded using Shannon-Fano coding.
        '''
        args = list(parse_args(args))
        radix = int(args.pop(0))
        probs = list(map(Fraction, args))
        result = information_theory.calculate_shannon_fano_avg_len(radix, probs)
        if all(is_decimal(x) for x in args):
            result = float(result)
        print(f"average length of code is {result}")


def parse_args(args):
    # tuple cause we don't want the arguments to be mutated :)
    return tuple(args.split())
