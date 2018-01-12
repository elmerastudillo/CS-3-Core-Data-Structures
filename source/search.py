#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests

    # If index is bigger than the length of the array return None
    if index < len(array):
        if item == array[index]:
            return index
        index = index + 1
        return linear_search_recursive(array, item, index)
    return None


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)
    return binary_search_iterative(array, item)



def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    left_bound = 0
    right_bound = (len(array) - 1)

    if array[left_bound] == item:
        return left_bound
    elif array[right_bound] == item:
        return right_bound

    while left_bound <= right_bound:
        middle = int((left_bound + right_bound) / 2)
        print("This is my middle {}".format(middle))
        print("This is the leftbound {} and rightbound {}".format(left_bound, right_bound))
        if item == array[middle]:
            return middle
        if array[middle] < item:
            left_bound = middle + 1
        if array[middle] > item:
            right_bound = middle - 1



    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    #TODO: implement binary search recursively here

    # Setting the left and right index
    # Left index is the 0
    # Right index is the 
    if left is None and right is None:
        left = 0
        right = (len(array) - 1)

    # Middle is the left + right index / 2
    middle = int((left + right) / 2)

    # If item is equal the middle index of the array return index
    if item == array[middle]:
        return middle

    # If middle item is less than item the mode the left index plus one
    if array[middle] < item:
        left = middle + 1

    # If middle item is more than item the mode the left index plus one 
    if array[middle] > item:
        right = middle - 1

    # If the left index surpassed the right index then return None
    if left > right:
        return None
        
    print("left " + str(left))
    print("right " + str(right))
    return binary_search_recursive(array, item, left, right)

    
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
names = ['Alex', 'Brian', 'Julia', 'Kojin', 'Nabil', 'Nick', 'Winnie']
middle = binary_search_recursive(names, 'Alex')
print("This is the item we are looking for: {}".format(middle))
# binary_search_recursive(names, 'Winnie')
# linear_search_recursive(names, "Nick")


