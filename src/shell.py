import cmd
import re
from ast import literal_eval
from fractions import Fraction
from functools import wraps

from colorama import Fore

from src.ch2 import error_correction
from src.ch3 import (
    arithmetic_code,
    comma_code,
    dictionary_code,
    huffman_code,
    kraft_mcmillan,
)
from src.ch4 import information_theory
from src.ch5 import number_theory, primality_testing
from src.ch6 import algebraic_coding
from src.ch7 import ciphers, cryptography


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
    intro = (
        "Welcome to the MATH3411 Shell.\n"
        'Type "help" or "?" to list commands. '
        'Type "exit" or ctrl-d to exit.'
    )
    prompt = f"{Fore.GREEN}> {Fore.RESET}"

    def do_exit(self, args):
        """
        Exit MATH3411 shell.
        """
        print()
        return True

    def do_EOF(self, args):
        """
        Exit MATH3411 shell.
        """
        return self.do_exit(args)

    # Ch2. Error Correction and Detection

    @do_help_on_error
    def do_is_isbn(self, args):
        """
        Usage: is_isbn ISBN

        Check a number satisfies the ISBN-10 check condition.
        """
        print(error_correction.is_isbn(*parse_args(args)))

    @do_help_on_error
    def do_isbn_fix(self, args):
        """
        Usage: isbn_fix ISBN ERROR_DIGIT

        Correct the nth digit in a given ISBN-10 number.
        """
        result = error_correction.isbn_fix(*parse_args(args))
        if result != -1:
            print(f"Correct digit is {result}")
        else:
            print("Could not find correct digit")

    @do_help_on_error
    def do_weight(self, args):
        """
        Usage: weight CODEWORD

        Find the weight of given codewords. That is, the distance between a
        codeword and the zero-codeword, or the number of non-zero values in each
        codeword.
        """
        codewords = parse_args(args)
        result = error_correction.get_weight(codewords)
        for codeword, weight in zip(codewords, result):
            print(f"Weight of {codeword} is {weight}")

    @do_help_on_error
    def do_distance(self, args):
        """
        Usage: distance CODEWORD1 CODEWORD2

        Find the distance between two codewords. That is, the number of values
        that differ for each position in the codewords.
        """
        result = error_correction.get_distance(*parse_args(args))
        print(f"Distance is {result}")

    @do_help_on_error
    def do_congruence(self, args):
        """
        Usage: congruence a m [b]

        Evaluate linear congruences a*x ≡ b (mod m).
        """
        args = list(map(int, parse_args(args)))
        target = args.pop(2) if len(args) > 2 else None
        result = error_correction.eval_congruence(*args, b=target)
        if target:
            if result is not None:
                print(f"x is {result}")
            else:
                print("There is no solution.")

    @do_help_on_error
    def do_modular_inverse(self, args):
        """
        Usage: modular_inverse a m

        Find n where n ≡ a^-1 (mod m)
        """
        args = list(map(int, parse_args(args)))
        result = error_correction.eval_congruence(*args, b=1)
        if result is not None:
            print(f"x is {result}")
        else:
            print("There is no solution.")

    @do_help_on_error
    def do_add_codewords(self, args):
        """
        Usage: add_codewords RADIX CODEWORD1 CODEWORD2 [CODEWORDS...]

        Add codewords of a given radix together.
        """
        result = error_correction.add_codewords(*parse_args(args))
        print(result)

    # Ch3. Compression Coding

    @do_help_on_error
    def do_kraft_mcmillan(self, args):
        """
        Usage: kraft_mcmillan RADIX LENGTH [LENGTHS...]

        Evaluate Kraft-McMillan inequality
        """
        args = list(map(int, parse_args(args)))
        result = kraft_mcmillan.eval_kraft_mcmillan(*args)
        print(f"K = {result} = {float(result)}")
        print(f"K ≤ 1 is {result <= 1}")

    @do_help_on_error
    def do_kraft_mcmillan_length(self, args):
        """
        Usage: kraft_mcmillan_length K RADIX LENGTH [LENGTHS...]

        Find the missing codeword length that satisifes the Kraft-McMillan
        Theorem given the coefficient K, radix and other codeword lengths
        """
        args = parse_args(args)
        k = Fraction(args[0])
        radix = int(args[1])
        lengths = [int(length) for length in args[2:]]
        result = kraft_mcmillan.eval_kraft_mcmillan_length(k, radix, *lengths)

        print(f"length is {result}")
        result_args = [str(x) for x in [radix] + lengths + [result]]
        self.do_kraft_mcmillan(" ".join(result_args))

    @do_help_on_error
    def do_kraft_mcmillan_min_length(self, args):
        """
        Usage: kraft_mcmillan_min_length RADIX LENGTH [LENGTHS...]

        Find the minimum codeword length that satisifes the Kraft-McMillan
        Theorem given the radix and other codeword lengths
        """
        args = list(map(int, parse_args(args)))
        result = kraft_mcmillan.eval_kraft_mcmillan_min_length(*args)

        print(f"length is {result}")
        result_args = [str(x) for x in args + [result]]
        self.do_kraft_mcmillan(" ".join(result_args))

    @do_help_on_error
    def do_kraft_mcmillan_radix(self, args):
        """
        Usage: kraft_mcmillan_radix LENGTH [LENGTHS...]

        Find the minimum radix that satisifes the Kraft-McMillan Theorem given
        the codeowrd lengths
        """
        args = list(map(int, parse_args(args)))
        result = kraft_mcmillan.eval_kraft_mcmillan_radix(*args)
        if result != -1:
            print(f"radix is {result}")
        else:
            print("length > 100")

    @do_help_on_error
    def do_comma_encode(self, args):
        """
        Usage: comma_encode LENGTH MESSAGE

        Encode a message using a comma code of a given length
        Note: message is expected to be in format 's1s2s3s4'
        """
        args = list(parse_args(args))
        length = int(args.pop(0))
        result = comma_code.comma_encode(length, *args)
        print(f"encoded message is '{result}'")

    @do_help_on_error
    def do_comma_decode(self, args):
        """
        Usage: comma_decode LENGTH MESSAGE

        Decode a message encoded using a comma code of a given length
        """
        args = list(parse_args(args))
        length = int(args.pop(0))
        result = comma_code.comma_decode(length, *args)
        print(f"decoded message is '{result}'")

    @do_help_on_error
    def do_lz78_encode(self, args):
        """
        Usage: lz78_encode MESSAGE

        Encodes a message using the LZ78 algorithm.
        """
        result = dictionary_code.lz78_encode(*parse_args(args))
        print("no. entry      output")
        for index, entry in enumerate(result):
            print(f"{index+1:<3d} {entry[0]:10} {entry[1]}")

    @do_help_on_error
    def do_lz78_decode(self, args):
        """
        Usage: lz78_decode OUTPUT [OUTPUTS...]

        Decode a message encoded with the LZ78 algorithm.
        """
        outputs = map(
            lambda s: re.sub(r"([a-zA-Z])", r"'\1'", s), parse_args(args)
        )
        outputs = list(map(literal_eval, outputs))
        result = dictionary_code.lz78_decode(outputs)
        print(f"message is '{result}'")

    @do_help_on_error
    def do_arithmetic_encode(self, args):
        """
        Usage: arithmetic_encode SOURCE_SYMBOLS SOURCE_PROBABILITIES MESSAGE

        Encode a message using arithmetic encoding with the provided source
        symbols and their respective probabilities.
        Note: symbols must be 1 char long.
        Note: you can use anything as a stop symbol as long as YOU know it's
        the stop symbol.
        """
        args = list(parse_args(args))

        source = list(args.pop(0))
        msg = args.pop()
        probabilities = list(map(float, args))
        result = arithmetic_code.arithmetic_encode(source, probabilities, msg)
        print(f"a valid value would be {result:.5f}")

    @do_help_on_error
    def do_arithmetic_decode(self, args):
        """
        Usage: arithmetic_decode SOURCE_SYMBOLS SOURCE_PROBABILITIES VALUE

        Decode an arithmetic encoded message using the provided source symbols
        and their respsective probabilities.
        Note: symbols must be 1 char long.
        Note: you can use anything as a stop symbol as long as YOU know it's
        the stop symbol.
        """
        args = list(parse_args(args))

        source = list(args.pop(0))
        probabilities = list(map(float, args))
        value = probabilities.pop()
        result = arithmetic_code.arithmetic_decode(source, probabilities, value)
        print(f"decoded message is {result}")

    @do_help_on_error
    def do_huffman_avg_len(self, args):
        """
        Usage: huffman_avg_len RADIX PROBABILITY [PROBABILITIES...]

        Calculates the average length of a Huffman code of the given radix
        and probabilities.
        """
        args = list(parse_args(args))
        radix = int(args.pop(0))
        probabilities = list(map(Fraction, args))
        result = huffman_code.calculate_huffman_avg_len(radix, probabilities)
        print(f"average length of code is {result}")

    @do_help_on_error
    def do_huffman_generate(self, args):
        """
        Usage: huffman_generate RADIX PROBABILITY [PROBABILITIES...]

        Generate a Huffman code based on the given radix and probabilities of
        source symbols. The code is generate using the "place high strategy".
        """
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
        """
        Usage: entropy RADIX PROBABILITY [PROBABILITIES...]

        Calculate the entropy for given probabilities and radix.
        """
        args = list(parse_args(args))
        radix = int(args.pop(0))
        probabilities = list(map(Fraction, args))
        result = information_theory.calculate_entropy(radix, probabilities)
        print(f"entropy is {result}")

    @do_help_on_error
    def do_shannon_fano(self, args):
        """
        Usage: entropy RADIX PROBABILITY [PROBABILITIES...]

        Generate a table indicating the lengths of symbols with provided
        probabilities if they were encoded using the Shannon-Fano code.
        """
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
        """
        Usage: entropy RADIX PROBABILITY [PROBABILITIES...]

        Given the radix and source probabilities, calculate the average length
        if a message encoded using Shannon-Fano coding.
        """
        args = list(parse_args(args))
        radix = int(args.pop(0))
        probs = list(map(Fraction, args))
        result = information_theory.calculate_shannon_fano_avg_len(radix, probs)
        if all(is_decimal(x) for x in args):
            result = float(result)
        print(f"average length of code is {result}")

    # Ch5. Algebra and Number Theory

    @do_help_on_error
    def do_gcd(self, args):
        """
        Usage: gcd NUMBER1 NUMBER2

        Calculate the greatest common divisor of 'a' and 'b', gcd(a, b), using
        the Euclidean Algorithm with
        a = NUMBER1
        b = NUMBER2
        """
        args = list(map(int, parse_args(args)))
        gcd, eqns = number_theory.calculate_gcd(*args)
        for a, b, q, r in eqns:
            print(f"{a:5} = {b:<5} * {q} + {r}")
        print(f"gcd is {gcd}")

    @do_help_on_error
    def do_bezout_identity(self, args):
        """
        Usage: bezout_identity GCD NUMBER1 NUMBER2

        Evaluate the values of x and y Bezout's Identity. That is find x and y
        in d = gcd(a, b) = ax + by with
        d = GCD
        a = NUMBER1
        b = NUMBER2
        """
        args = list(map(int, parse_args(args)))
        x, y = number_theory.solve_bezout_identity(*args)
        print(f"x is {x}, y is {y}")

    @do_help_on_error
    def do_eulers_phi(self, args):
        """
        Usage: eulers phi NUMBER

        Find the number of 'units' in Z_m (integer modular).
        That is the number of elements in set {a ∈ Z_m: gcd(a, m) = 1}
        """
        args = list(map(int, parse_args(args)))
        a = args.pop(0)
        result = number_theory.find_eulers_phi(a, *args)
        print(f"ϕ({a}) = {result}")

    @do_help_on_error
    def do_order(self, args):
        """
        Usage: order MOD_BASE NUMBER

        Find the order of a number for a given modular base.
        """
        args = list(map(int, parse_args(args)))
        result = number_theory.find_order(*args)
        if result != -1:
            print(f"order is {result}")
        else:
            print("order is greater than the modular base")

    @do_help_on_error
    def do_primitive_elements(self, args):
        """
        Usage: primitive_elements NUMBER

        Find the primitive elements of a given number.
        """
        args = list(map(int, parse_args(args)))
        result = number_theory.find_primitive_elements(*args)
        if result:
            print(f"primitives are {result}")
            print(f"no. of primitives is {len(result)}")
        else:
            print("there are no primitive elements")

    def do_is_prime(self, args):
        """
        Usage: is_prime N

        Evaluate whether N is prime or not
        """
        args = list(map(int, parse_args(args)))
        for a in args:
            result = primality_testing.is_prime(a)
            prime_val = "prime" if result else "not prime"
            print(f"{a} is {prime_val}")

    def do_generate_primes(self, args):
        """
        Usage: generate_primes N

        Generate all prime numbers less than or equal to N
        """
        args = list(map(int, parse_args(args)))
        result = primality_testing.generate_primes(*args)
        print(result)

    @do_help_on_error
    def do_pseudo_prime(self, args):
        """
        Usage: pseudo_prime N BASE [BASES...]

        Evaluate whether N is pseudo-prime to the given bases using the
        pseudo-prime test.
        """
        args = list(map(int, parse_args(args)))
        n = args.pop(0)
        print(f"{n} is pseudo-prime to base")
        for a in args:
            result = primality_testing.is_pseudo_prime(n, a)
            colour = Fore.GREEN if result else Fore.RED
            print(f"{a} is {colour}{result}{Fore.RESET}")

    @do_help_on_error
    def do_lucas_prime_test(self, args):
        """
        Usage: lucas_prime_test N BASE [BASES...]

        Evaluate whether N is prime to the given bases using Lucas' test.
        """
        args = list(map(int, parse_args(args)))
        n = args.pop(0)
        print(f"{n} is pseudo-prime to base")
        for a in args:
            result = primality_testing.is_prime_lucas_test(n, a)
            colour = Fore.GREEN if result else Fore.RED
            print(f"{a} is {colour}{result}{Fore.RESET}")

    @do_help_on_error
    def do_strong_pseudo_prime(self, args):
        """
        Usage: strong_pseudo_prime N BASE [BASES...]

        Evaluate whether N is a strong pseudo-prime to the given bases using
        the Miller-Rabin primality test
        """
        args = list(map(int, parse_args(args)))
        n = args.pop(0)
        print(f"{n} is pseudo-prime to base")
        for a in args:
            result = primality_testing.is_strong_pseudo_prime(n, a)
            colour = Fore.GREEN if result else Fore.RED
            print(f"{a} is {colour}{result}{Fore.RESET}")

    @do_help_on_error
    def do_fermat_factorise(self, args):
        """
        Usage: fermat_factorise N

        Fermat factorise N where N is an add integer.
        """
        args = list(map(int, parse_args(args)))
        n = args.pop(0)
        (a, b) = primality_testing.fermat_factorise(n, *args)
        print(f"{n} = {a}*{b}")

    # Ch6. Algebraic Coding
    @do_help_on_error
    def do_cyclotomic_set(self, args):
        """
        Usage: cyclotomic_set BASE POWER [K_BASE...]
        """
        args = list(map(int, parse_args(args)))
        result = algebraic_coding.cyclotomic_set(*args)
        for k, v in result.items():
            print(k, v)

    # Ch7. Cryptography

    @do_help_on_error
    def do_caesar_cipher(self, args):
        """
        Usage: caesar_cipher MESSAGE

        Shift a message using the Caesar cipher.
        """
        result = ciphers.shift_cipher(3, *parse_args(args))
        print(result)

    @do_help_on_error
    def do_shift_cipher(self, args):
        """
        Usage: shift_cipher SHIFT MESSAGE

        Shift a message using a given shift.
        """
        args = list(parse_args(args))
        shift = int(args.pop(0))
        result = ciphers.shift_cipher(shift, *args)
        print(result)

    @do_help_on_error
    def do_vigenere_encode(self, args):
        """
        Usage: vigenere_encode KEY MESSAGE

        Encode a message with the vigenere cipher using the given key.
        """
        result = ciphers.vigenere_cipher(*parse_args(args), decode=False)
        print(result)

    @do_help_on_error
    def do_vigenere_decode(self, args):
        """
        Usage: vigenere_decode KEY MESSAGE

        Decode a message with the vigenere cipher using the given key.
        """
        result = ciphers.vigenere_cipher(*parse_args(args), decode=True)
        print(result)

    @do_help_on_error
    def do_plaintext_feedback_encode(self, args):
        """
        Usage: plaintext_feedback_encode KEY MESSAGE

        Encode a message using the plaintext feedback cipher.
        """
        result = ciphers.plaintext_feedback_encode(*parse_args(args))
        print(result)

    @do_help_on_error
    def do_plaintext_feedback_decode(self, args):
        """
        Usage: plaintext_feedback_decode KEY MESSAGE

        Decode a message encoded using the plaintext feedback cipher.
        """
        result = ciphers.plaintext_feedback_decode(*parse_args(args))
        print(result)

    @do_help_on_error
    def do_ciphertext_feedback_encode(self, args):
        """
        Usage: ciphertext_feedback_encode KEY MESSAGE

        Encode a message using the ciphertext feedback cipher.
        """
        result = ciphers.ciphertext_feedback_encode(*parse_args(args))
        print(result)

    @do_help_on_error
    def do_ciphertext_feedback_decode(self, args):
        """
        Usage: ciphertext_feedback_decode KEY MESSAGE

        Decode a message encoded using the ciphertext feedback cipher.
        """
        result = ciphers.ciphertext_feedback_decode(*parse_args(args))
        print(result)

    @do_help_on_error
    def do_feedback_cipher_encode(self, args):
        """
        Usage: feedback_cipher_encode KEY MESSAGE

        Encode a message using the plaintext and ciphertext feeback cipher and
        output the corresponding ciphertext for each encoding.
        """
        args = parse_args(args)
        plaintext = ciphers.plaintext_feedback_encode(*args)
        ciphertext = ciphers.ciphertext_feedback_encode(*args)
        print(f"plaintext : {plaintext}")
        print(f"ciphertext: {ciphertext}")

    @do_help_on_error
    def do_feedback_cipher_decode(self, args):
        """
        Usage: feedback_cipher_decode KEY MESSAGE

        Decode a message using the plaintext and ciphertext feeback cipher and
        output the corresponding plaintext for each encoding.
        Useful when figuring out whether a message was encoded using plaintext
        or ciphertext feedback.
        """
        args = parse_args(args)
        plaintext = ciphers.plaintext_feedback_decode(*args)
        ciphertext = ciphers.ciphertext_feedback_decode(*args)
        print(f"plaintext : {plaintext}")
        print(f"ciphertext: {ciphertext}")

    @do_help_on_error
    def do_index_of_coincidence(self, args):
        """
        Usage: index_of_coincidence MESSAGE

        Calculate the index of coincidence of a given message.
        """
        result = ciphers.index_of_coincidence(*parse_args(args))
        print(f"index of coincidence is {result} ({float(result)})")

    @do_help_on_error
    def do_estimate_key_length(self, args):
        """
        Usage: estimate_key_length MESSAGE

        Estimate the key length of an encrypted message.
        """
        result = ciphers.estimate_key_len(*parse_args(args))
        print(f"r ≈ {result}")

    @do_help_on_error
    def do_rsa_exponent_key(self, args):
        """
        Usage: rsa_exponent_key N EXPONENT

        Find the corresponding exponent given N and the other exponent key
        That is, if we have the encryption exponent, find decryption exponent
        and vice versa.
        """
        args = list(map(int, parse_args(args)))
        result = cryptography.rsa_exponent_key(*args)
        print(f"d = {result}")

    @do_help_on_error
    def do_rsa_encrypt(self, args):
        """
        Usage: rsa_encrypt N EXPONENT MESSAGE
        """
        args = list(parse_args(args))
        n = int(args.pop(0))
        e = int(args.pop(0))
        result = cryptography.rsa_encrypt_scheme(1, n, e, *args)
        print(result)

    @do_help_on_error
    def do_rsa_decrypt(self, args):
        """
        Usage: rsa_decrypt N EXPONENT MESSAGE
        """
        args = list(map(int, parse_args(args)))
        result = cryptography.rsa_decrypt_scheme(1, *args)
        print(result)

    @do_help_on_error
    def do_rsa_encrypt_scheme(self, args):
        """
        Usage: rsa_encrypt_scheme SCHEME N EXPONENT MESSAGE
        """
        args = list(parse_args(args))
        scheme = int(args.pop(0))
        n = int(args.pop(0))
        e = int(args.pop(0))
        result = cryptography.rsa_encrypt_scheme(scheme, n, e, *args)
        print(result)

    @do_help_on_error
    def do_rsa_decrypt_scheme(self, args):
        """
        Usage: rsa_decrypt_scheme SCHEME N EXPONENT MESSAGE
        """
        args = list(map(int, parse_args(args)))
        result = cryptography.rsa_decrypt_scheme(*args)
        print(result)


def parse_args(args):
    # tuple cause we don't want the arguments to be mutated :)
    return tuple(args.split())
