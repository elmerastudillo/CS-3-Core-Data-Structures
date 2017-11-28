#!python
import pdb

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order."""
    # Check that all adjacent items are in order, return early if not
    # for i in range(len(items) - 1):
    #     if items[i] > items[i + 1]:
    #         continue
    #     else:
    #         return False
    # return True

    for index, item in enumerate(items):
        if index+1 < len(items):
        # If item is larger than succeeding item, return False
            if item > items[index+1]:
                return False
    return True


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order."""
    # Repeat until all items are in sorted order
    # Swap adjacent items that are out of order
    # loop through list
    while not is_sorted(items):
        for i in range(len(items) - 1):
            # Loop backwards avoiding the already sorted numbers
            for j in range(len(items) - 1 - i):
                # if left item is bigger than the right
                if items[j] > items[j + 1]:
                    # Swap left and right 
                    items[j], items[j + 1] = items[j + 1], items[j]
        return items




def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order."""
    # Repeat until all items are in sorted order
    # Find minimum item in unsorted items
    # Swap it with first unsorted item
    # pdb.set_trace()
    while not is_sorted(items):
        for i in range(len(items) - 1):
            # setting the minimum to start with
            min = i
            # Start looping from the current index i
            for j in range(i + 1, len(items)):
                # if j is less than our current minimum
                if items[j] < items[min]:
                    # set j to our minimum
                    min = j
            # Once loop is done set i to be our minimum
            items[i], items[min] = items[min], items[i]
        return items




def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order."""
    # Repeat until all items are in sorted order
    # Take first unsorted item
    # Insert it in sorted order in front of items

    # NOTE: Need to be able to sort multiples
    while not is_sorted(items):
        # 
        for i in range(len(items)-1):
            # Loop through the list in reversal until you get to 0
            for j in range(i, - 1, -1):
                # If left index is bigger than right index
                if items[j] > items[j + 1]:
                    # Then swap
                    items[j], items[j + 1] = items[j + 1], items[j]
                else:
                    # Break once the item is not bigger and insert
                    break
        return items




def test_sorting(sort=selection_sort, num_items=20, max_value=50):
    """Test sorting algorithms with a small list of random items."""
    # Create a list of 8 or 16 items in arbitrary order
    # items = [3, 5, 4, 2, 6, 8, 1, 7]
    # items = [11, 13, 8, 4, 12, 2, 14, 3, 5, 18, 6, 10, 1, 7, 9, 15]

    # Create a list of items randomly sampled from range [1...max_value]
    import random
    items = random.sample(range(1, max_value + 1), num_items)
    # item_range = list(range(1, max_value + 1))
    # items = [random.choice(item_range for _ in range(num_items))]
    print('Initial items: {!r}'.format(items))

    # Change this sort variable to the sorting algorithm you want to test
    sort = selection_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        sort = globals()[sort_name]
    else:
        sort = bubble_sort

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
    except:
        print('Integer required for `num` and `max` command-line arguments')

    # Test sort function, but don't explode if sort function does not exist
    try:
        test_sorting(sort, num_items, max_value)
    except NameError:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('\trandomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')


if __name__ == '__main__':
    # main()
    unsorted_list = [6, 5, 4, 3, 2, 1]
    # sorted_list = bubble_sort(unsorted_list)
    # print(sorted_list)
    # sorted_list = selection_sort(unsorted_list)
    # print(sorted_list)
    # print(unsorted_list)
    sorted_list = insertion_sort(unsorted_list)
    print(sorted_list)
    # print(selection_sort(unsorted_list))
    # new_list = bubble_sort(unsorted_list)
    # print(bubble_sort(unsorted_list))
    # print(new_list)
