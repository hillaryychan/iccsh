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

def parse_args(args):
    return tuple(args.split(' '))

if __name__ == '__main__':
    ICCShell().cmdloop()
