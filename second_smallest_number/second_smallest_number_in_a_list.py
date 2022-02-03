'''
Given a list of numbers, return the second smallest number.
'''

# Solution #1
# Python program to find largest, smallest, second largest and second smallest elements
def second_smallest(list):
    length = len(list)
    list.sort()
    print("Largest Element: ", list[length - 1])
    print("Smallest Element: ", list[0])
    print("Second Largest Element: ", list[length - 2])
    print("Second Smallest Element: ", list[1])

list = [2, 5, 1, 0, 6]
range = second_smallest(list)


# Solution #2
# Python program to find smallest and second smallest elements
import sys
import random
import operator
from typing import List, Tuple

def second_smallest(lst: List[int]) -> Tuple[List, int, int]:

    # there should be at least two elements
    if len(lst) < 2:
        msg = "Invalid Input"
        return lst, msg, msg

    absolute_low = second_smallest = sys.maxsize
    for elem in lst:

        # current element is lower than lowest?
        if elem < absolute_low:

            # make (currently) lowest a second_smallest: we found lower
            second_smallest = absolute_low
            # then assign this all-time low as absolute
            absolute_low = elem

        # current element in between absolute low and second-smallest?
        elif absolute_low < elem < second_smallest:

            # update second_smallest
            second_smallest = elem

    if operator.eq(second_smallest, sys.maxsize):
        print("No second smallest element")
    return lst, absolute_low, second_smallest


# Test
if __name__ == '__main__':
    if __import__('sys').version_info.major < 3:
        print('Tested with Python 3')

    line = 'Given list is %s: Smallest: %d, Second smallest (next higher): %d'
    list_generator = lambda: (random.randrange(-5, 50) for n in range(10))
    for l in (list_generator for _ in range(10)):
        list_ = list(l())
        print(line % second_smallest(list_))
