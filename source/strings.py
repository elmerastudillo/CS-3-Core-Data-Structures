#!python

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    if pattern == '':
        return True
        
    found_word = find_index(text, pattern)
    if found_word is None:
        return False
    else:
        return True



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    # Storing index of current text
    current_index = 0
    # Storing index of current place in pattern
    current_pattern_index = 0
    # Edge case if pattern is empty
    if pattern == '':
            return 0

    # If current index is less then legnth of text then keep looping
    while current_index <= len(text) - 1:
        print("Does {} and this {} match".format(text[current_index],pattern[current_pattern_index]))
        # If the index in text and the index in the pattern are equal
        if text[current_index] == pattern[current_pattern_index]:
            # Incremenet the current_pattern index by 1 to check the next letter 
            current_pattern_index = current_pattern_index + 1
            # if the length of the pattern is equal to the current_pattern_index we 
            # found the word
            if len(pattern) == current_pattern_index:
                print("word was found")
                # Getting the index of the first letter of the pattern
                final_index = current_index - (current_pattern_index - 1)
                print("This is the final index {}".format(final_index))
                return final_index
        else:
            # If pattern index is more than 0
            if current_pattern_index > 0:
                # Check the last letter checked against the pattern from the beggining
                current_index = current_index - 1
                # Return it to 0 to start the check over again
                current_pattern_index = 0
        print("This is the current index {}".format(current_index))
        # Increment the index by 1
        current_index += 1
    return None
            
        

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)

    # Need to find a way to search through the same text multiple times for the pattern staring 
    # from the last index we searched
    # ummmm! 
    found_indexes = []
    i = 0
    while i != len(text):
        index = find_index(text,pattern)
        found_indexes.append(index)
        i = i + 1
    if found_indexes is not None:
        return []
    else:
        return found_indexes


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
    main()
