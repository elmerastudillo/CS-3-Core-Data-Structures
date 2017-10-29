def binary_search_recursive(array, item, left=None, right=None):

def binary_search_iterative(array, item):
    """iteratively return the index of the item with binary search or None if not found"""
    # First, set the lower_index = 0 
    # upper_index as the length of array -1 
    lower_index = 0
    upper_index = len(array) - 1

    while lower_index <= upper_index:
        # calculate the middle index by sum the lower_index and upper_index and divide by 2
        middle_index = (lower_index + upper_index) // 2 # // is int division
        # check if the item is found
        if array[middle_index] == item:
            return middle_index
        # added the comment for line 15-18
        elif array[middle_index] > item:
            upper_index = middle_index - 1
        elif array[middle_index] < item:
            lower_index = middle_index + 1
        # Did not find
    return None