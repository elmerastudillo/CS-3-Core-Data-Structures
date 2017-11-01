#!python
import re

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    clean_text = re.sub('[^A-Za-z]+', '', text).lower().split()
    # word_array = clean_text.split()
    # print(word_array)
    for w in clean_text:
        print(w)
        # print(pattern)
        if pattern == w:
            return True
    return False



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    clean_text = re.sub(r'[^A-Za-z ]+', '', text).lower()
    try:
        return clean_text.index('zzzzzzz')
    except ValueError:
         return None


def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    print(contains("name", "n"))
    # print(find_index("hi name is", "name"))


# def find_word_in_sentence(sentence, word):
#     clean_sentence = re.sub('[^A-Za-z]+', '', text).lower()
#     word_array = clean_sentence.split()
#     for w in word_array:
#         if w == word:
#             return True
#     return False
#
# def find_letter_in_sentence(letter, sentence):
#
#
#
# def find_letter_in_word(word, letter):
#     for l in word:
#         if l == letter:
#             return True
#     return False
#
# print(find_word_in_sentence("hi my name is elmer", "elmer"))
# print(find_letter_in_word("hello", "h"))
