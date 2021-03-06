#!python
import pdb
import random

def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order."""
    # TODO: Running time: ??? Why and under what conditions?
    # TODO: Memory usage: ??? Why and under what conditions?"""
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
    # TODO: Running time: ??? Why and under what conditions?
    # TODO: Memory usage: ??? Why and under what conditions?"""
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
    # TODO: Running time: ??? Why and under what conditions?
    # TODO: Memory usage: ??? Why and under what conditions?"""
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
    # TODO: Running time: ??? Why and under what conditions?
    # TODO: Memory usage: ??? Why and under what conditions?"""
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

    """Order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order. """
    # TODO: Running time: O(n + m), where n is the size of items 1 and m is the size of items 2
    # TODO: Memory usage: ??? Why and under what conditions
    # TODO: Repeat until one list is empty
    left_index = 0
    right_index = 0
    merge_list = []
    while (left_index < len(items1)) and (right_index < len(items2)):
    # TODO: Find minimum item in both lists and append it to new list
        if items1[left_index] > items2[right_index]:
            merge_list.append(items2[right_index])
            right_index += 1
        elif items1[left_index] < items2[right_index]:
            merge_list.append(items1[left_index])
            left_index += 1
        elif items1[left_index] == items2[right_index]:
            merge_list.append(items1[left_index])
            merge_list.append(items2[right_index])
            right_index += 1
            left_index += 1
    # TODO: Append remaining items in non-empty list to new list
    if left_index == len(items1):
        merge_list.extend(items2[right_index:])
    elif right_index == len(items2):
        merge_list.extend(items1[left_index:])

    # Alternate solution
    # Add remaining items to merge_sort list from either items1 or items2
    # Only one is guaranteed to run 
    # for index in range(left_index, len(items1)):
    #     merge_sort.append(index)

    # for index in range(right_index, len(items1)):    
    #     merge_sort.append(index)
    return merge_list
    



def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order. """
    # TODO: Running time: ??? Why and under what conditions?
    # TODO: Memory usage: ??? Why and under what conditions?
    # Split items list into approximately equal halves
    pivot = int(len(items)/2)
    first_half = items[:pivot]
    second_half = items[pivot:]
    # TODO: Sort each half using any other sorting algorithm
    while not is_sorted(first_half):
        bubble_sort(first_half)

    while not is_sorted(second_half):
        insertion_sort(second_half)
    # TODO: Merge sorted halves into one list in sorted order
    # Why does this mutate when we use list[:]
    items[:] = merge(first_half,second_half)


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order. """
    # Running time: O(nlogn) Best and Worst case
    # Memory usage: O(nlogn) 
    # Check if list is so small it's already sorted (base case)
    if len(items) > 1:
    # Split items list into approximately equal halves
        pivot = len(items)//2
        first_half = items[:pivot]
        second_half = items[pivot:]
        # Sort each half by recursively calling merge sort
        merge_sort(first_half)
        merge_sort(second_half)
        # Merge sorted halves into one list in sorted order
        items[:] = merge(first_half,second_half)

def quick_sort(items, low = 0, high = -1):
    """Sort given items by finding the pivot of the list 
    and then sorting the left side and right side of the pivot recursively. """
    if high == -1:
        high = len(items) - 1 

    if low  < high:
        pivot = partition(items, low, high)
        # Left side of pivot
        quick_sort(items, low, pivot - 1)
        # Right side of pivot
        quick_sort(items, pivot + 1, high)

# def swap(items, first_index):
#     temp = items[first_index + 1]
#     last = len(items) - 1
#     items[first_index + 1] = items[]
#     items[last] = temp


def partition(items, low, high):
    """We set the high index as the pivot and then move all the less then numbers
     to the left of the pivot and more then numbers to the right side of the pivot."""
    # Selecting pivot as far right number
    pivot = items[high]
    i = low - 1
    j = low
    while j <= high - 1:
        print(j)
        # If the value in index j is less than the pivot
        if items[j] <= pivot:
            # We increate the index of i by 1
            i += 1
            # Swap the values in index i and j
            items[i], items[j] = items[j], items[i]
        # Increase the index of J by 1 after every check
        j += 1
    # Swap the pivot with the index after i (i + 1)
    temp = items[i + 1]
    items[i + 1] = pivot
    items[high] = temp
    # Return the pivot
    return i + 1

def random_ints(count=20, min=1, max=50):
    """Return a list of `count` integers sampled uniformly at random from
    given range [`min`...`max`] with replacement (duplicates are allowed)."""
    import random
    return [random.randint(min, max) for _ in range(count)]


def test_sorting(sort=bubble_sort, num_items=20, max_value=50):
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
    quick_sort(unsorted_list, 0, len(unsorted_list) - 1)
    print(unsorted_list)
    # merge_sort(unsorted_list)
    # print(unsorted_list)
    # print(unsorted_list)
    # print(len(unsorted_list))
    # length = len(unsorted_list)
    # slist = quick_sort(unsorted_list, 0,length - 1)
    # print(quick_sort(unsorted_list, 0,length - 1))
    # merge_list = merge_sort(unsorted_list)
    # print(merge_list)
    # sorted_list = bubble_sort(unsorted_list)
    # print(sorted_list)
    # sorted_list = selection_sort(unsorted_list)
    # print(sorted_list)
    # print(unsorted_list)
    # sorted_list = insertion_sort(unsorted_list)
    # print(sorted_list)
    # print(selection_sort(unsorted_list))
    # new_list = bubble_sort(unsorted_list)
    # print(bubble_sort(unsorted_list))
    # print(new_list)

