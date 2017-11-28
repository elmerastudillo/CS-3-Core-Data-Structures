#!python
import pdb

def is_sorted(items):
<<<<<<< HEAD
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
=======
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check that all adjacent items are in order, return early if not
>>>>>>> 304f295769896473fc8929a5b86878716d52c4ac


def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
<<<<<<< HEAD
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


=======
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
>>>>>>> 304f295769896473fc8929a5b86878716d52c4ac


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
<<<<<<< HEAD
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


=======
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Find minimum item in unsorted items
    # TODO: Swap it with first unsorted item
>>>>>>> 304f295769896473fc8929a5b86878716d52c4ac


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
<<<<<<< HEAD
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
=======
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if list is so small it's already sorted (base case)
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half by recursively calling merge sort
    # TODO: Merge sorted halves into one list in sorted order


def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
>>>>>>> 304f295769896473fc8929a5b86878716d52c4ac
    """Test sorting algorithms with a small list of random items."""
    # Create a list of items randomly sampled from range [1...max_value]
    items = random_ints(num_items, 1, max_value)
    print('Initial items: {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))

    # Change this sort variable to the sorting algorithm you want to test
    sort = selection_sort
    print('Sorting items with {}(items)'.format(sort.__name__))
    sort(items)
    print('Sorted items:  {!r}'.format(items))
    print('Sorted order?  {!r}'.format(is_sorted(items)))


def main():
    """Read command-line arguments and test sorting algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name

    if len(args) == 0:
        script = sys.argv[0]  # Get script file name
        print('Usage: {} sort num max'.format(script))
        print('Test sorting algorithm `sort` with a list of `num` integers')
        print('    randomly sampled from the range [1...`max`] (inclusive)')
        print('\nExample: {} bubble_sort 10 20'.format(script))
        print('Initial items: [3, 15, 4, 7, 20, 6, 18, 11, 9, 7]')
        print('Sorting items with bubble_sort(items)')
        print('Sorted items:  [3, 4, 6, 7, 7, 9, 11, 15, 18, 20]')
        return

    # Get sort function by name
    if len(args) >= 1:
        sort_name = args[0]
        # Terrible hack abusing globals
        if sort_name in globals():
            sort_function = globals()[sort_name]
        else:
            # Don't explode, just warn user and show list of sorting functions
            print('Sorting function {!r} does not exist'.format(sort_name))
            print('Available sorting functions:')
            for name in globals():
                if name.find('sort') >= 0:
                    print('    {}'.format(name))
            return

    # Get num_items and max_value, but don't explode if input is not an integer
    try:
        num_items = int(args[1]) if len(args) >= 2 else 20
        max_value = int(args[2]) if len(args) >= 3 else 50
        # print('Num items: {}, max value: {}'.format(num_items, max_value))
    except ValueError:
        print('Integer required for `num` and `max` command-line arguments')
        return

    # Test sort function
    test_sorting(sort_function, num_items, max_value)


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
