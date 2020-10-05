import cmd
import utils


class ICCShell(cmd.Cmd):
    intro = (' Welcome to the MATH3411 Shell.\n'
             'Type help or ? to list commands. Type exit or ctrl-d to exit.')
    prompt = '> '

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

    def do_mod(self, args):
        '''
        mod a n
        Find the remainder of a / n
        '''
        args = [int(x) for x in parse_args(args)]
        utils.mod(*args)

    def do_mod_congruent(self, args):
        '''
        mod_congruent a n
        Finds the modular congruence b such that a ≡ b (mod n)
        '''
        args = [int(x) for x in parse_args(args)]
        utils.mod_congruent(*args)

    def do_is_isbn(self, args):
        '''
        Check a number satisfies the ISBN-10 check condition
        '''
        args = [x for x in parse_args(args)]
        print(utils.is_isbn(*args))

    def do_isbn_fix(self, args):
        '''
        Correct the nth digit in a given ISBN-10 number
        '''
        try:
            args = [x for x in parse_args(args)]
            result = utils.isbn_fix(*args)
            if result == -1:
                print("Could not find correct digit")
            else:
                print(f"Correct digit is {result}")
        except TypeError as exc:
            print(exc)


def parse_args(args):
    return tuple(args.split(' '))


if __name__ == '__main__':
    ICCShell().cmdloop()
