import cmd
import src.utils as utils

from colorama import Fore
from functools import wraps


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
        Exit MATH3411 shell
        '''
        print()
        return True

    def do_EOF(self, args):
        '''
        Exit MATH3411 shell
        '''
        return self.do_exit(args)

    def do_is_isbn(self, args):
        '''
        Usage: is_isbn ISBN

        Check a number satisfies the ISBN-10 check condition
        '''
        print(utils.is_isbn(*parse_args(args)))

    @do_help_on_error
    def do_isbn_fix(self, args):
        '''
        Usage: isbn_fix ISBN ERROR_DIGIT

        Correct the nth digit in a given ISBN-10 number
        '''
        result = utils.isbn_fix(*parse_args(args))
        if result != -1:
            print(f"Correct digit is {result}")
        else:
            print("Could not find correct digit")

    def do_weight(self, args):
        '''
        Usage: weight CODEWORD

        Find the weight of given codewords. That is, the distance between a
        codeword and the zero-codeword, or the number of non-zero values in each
        codeword.
        '''
        codewords = parse_args(args)
        result = utils.get_weight(codewords)
        for codeword, weight in zip(codewords, result):
            print(f"Weight of {codeword} is {weight}")

    def do_distance(self, args):
        '''
        Usage: distance CODEWORD1 CODEWORD2

        Find the distance between two codewords. That is, the number of values
        that differ for each position in the codewords.
        '''
        result = utils.get_distance(*parse_args(args))
        print(f"Distance is {result}")

    @do_help_on_error
    def do_congruence(self, args):
        '''
        Usage: congruence a m [b]

        Evaluate linear congruences a*x ≡ b (mod m)
        '''
        args = list(map(int, parse_args(args)))
        target = args.pop(2) if len(args) > 2 else None
        result = utils.eval_congruence(*args, b=target)
        if result is not None:
            print(f"x is {result}")

    @do_help_on_error
    def do_add_codewords(self, args):
        '''
        Usage: add_codewords RADIX CODEWORD1 CODEWORD2 [CODEWORDS...]

        Add codewords of a given radix together
        '''
        result = utils.add_codewords(*parse_args(args))
        print(result)


def parse_args(args):
    # tuple cause we don't want the arguments to be mutated :)
    return tuple(args.split(' '))
