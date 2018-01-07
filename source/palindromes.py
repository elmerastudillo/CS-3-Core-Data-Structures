#!python

import string
import re
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    # return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # TODO: implement the is_palindrome function iteratively here
    """Check if text is a palindrome iteratively"""
    # removing punctuation and converting all letters to lower case
    clean_text = remove_punctuation_and_remove_text(text)
    first_index = 0
    last_index = len(clean_text) - 1
    while first_index < len(clean_text):
        # If first index of text does not equal last index of text then return False
        if clean_text[first_index] != clean_text[last_index]:
            print("This is not a palindrome")
            return False
        else:
            # increment first and last index
            first_index += 1
            last_index -= 1
    return True




def is_palindrome_recursive(text, left=None, right=None):
    # TODO: implement the is_palindrome function recursively here
    if left is None and right is None:
        text = remove_punctuation_and_remove_text(text)
    print("This is the text: {}".format(text))
    if len(text) < 1 or text == '':
        return True

    if left is None and right is None:
        left = 0
        right = len(text) - 1
    print("These are the indexes: {}, {}".format(left, right))

    if left <= right:
        if text[left] == text[right]:
            is_palindrome_recursive(text, left=left + 1, right=right - 1)
        else:
            print("This is not a palindrome")
            return False
    print("This is a palindrome")
    return True
    # once implemented, change is_palindrome to call is_palindrome_recursive
    # to verify that your iterative implementation passes all tests

def remove_punctuation_and_remove_text(text):
    return ''.join([i for i in text.lower() if i in string.ascii_letters])


def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    # main()
    print(is_palindrome_iterative("knsjkn"))
