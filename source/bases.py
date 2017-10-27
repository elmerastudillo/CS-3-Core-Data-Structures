#!python

import string
import math
import re
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace
LCASE_SHIFT = 87
UCASE_SHIFT = 55

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)

    digits_length = len(digits)
    total = 0

    # TODO: Decode digits from binary (base 2)
    if base is 2:
        for index in range(digits_length):
            # Getting the number from binary by using the formula base^index * [value of index]
            number = math.pow(base, index) * int(digits[-index - 1])
            total += number
        print(total)
        return  total
    # ...
    # TODO: Decode digits from hexadecimal (base 16)
    if re.search('[a-zA-z]', digits):
        list_of_digits = list(digits)
        for i in list_of_digits:  
            if i.isupper():
                i = ord(i) - UCASE_SHIFT
            else if i.islower():
                i = ord(i) - LCASE_SHIFT 

    # ...
    # TODO: Decode digits from any base (2 up to 36)
    # ...
    if base > 2:
        for index in range(digits_length):
            # Getting the number from binary by using the formula base^index * [value of index]
            number = math.pow(base, index) * int(digits[-index - 1])
            total += number
        print(total)
        return total


def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    number_length_str = str(number)

    # TODO: Encode number in binary (base 2)
    # ...
    value = []
    binary_string = ""

    if base is 2:
        # While the number is still divisible
        while number > 0:
            # Get the remainder as the remainder is the actual binary digit
            remainder = number % base
            # set the number to be the whole number left after division
            number = int(number/base)
            # Insert the number into the beginning of the list (Prepend)
            value.insert(0, remainder)
        binary_string = ''.join(map(str, value))

        print(value)
        return binary_string

    # TODO: Encode number in hexadecimal (base 16)
    # ...
    if base is 16:
         while number > 0:
            # Get the remainder as the remainder is the actual binary digit
            remainder = number % base
            # set the number to be the whole number left after division
            number = int(number/base)
            # Insert the number into the beginning of the list (Prepend)
            value.insert(0, remainder)
        binary_string = ''.join(map(str, value))

    # TODO: Encode number in any base (2 up to 36)
    if base > 2:
        while number > 0:
            remainder = number % base
            number = int(number/base)
            value.insert(0, remainder)
        print(value)
        binary_string = ''.join(map(str, value))
        return binary_string
    # ...

#   


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
