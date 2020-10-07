import cmd
import src.utils as utils


class ICCShell(cmd.Cmd):
    intro = ('Welcome to the MATH3411 Shell.\n'
             'Type "help" or "?" to list commands. '
             'Type "exit" or ctrl-d to exit.')
    prompt = '\033[92m>\033[0m '

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

    def do_isbn_fix(self, args):
        '''
        Usage: isbn_fix ISBN ERROR_DIGIT

        Correct the nth digit in a given ISBN-10 number
        '''
        try:
            result = utils.isbn_fix(*parse_args(args))
            if result == -1:
                print("Could not find correct digit")
            else:
                print(f"Correct digit is {result}")
        except Exception as exc:
            print(exc)

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

    def do_congruence(self, args):
        '''
        Usage: congruence a m [b]

        Evaluate linear congruences a*x ≡ b (mod m)
        '''
        args = list(map(int, parse_args(args)))
        target = args.pop(2) if len(args) > 2 else None
        result = utils.eval_congruence(*args, b=target)
        if result:
            print(f"x is {result}")

    def do_add_codewords(self, args):
        '''
        Usage add_codewords RADIX CODEWORD1 CODEWORD2 [CODEWORDS...]

        Add codewords of a given radix together
        '''
        result = utils.add_codewords(*parse_args(args))
        print(result)


def parse_args(args):
    # tuple cause we don't want the arguments to be mutated :)
    return tuple(args.split(' '))
