# -*- coding: utf-8 -*-
def for_loop_with_index():
    """if for loop with index then use enumerate function

    >>> for_loop_with_index()
    (0, 1)
    (1, 3)
    (2, 7)
    (3, 10)
    """
    l = [1, 3, 7, 10]
    for i, element in enumerate(l):
        print(i, element)

    ## Bad pattern
    # i = 0
    # for element in l:
    #     print(i, element)
    #     i += 1

for_loop_with_index()


def swap_values(a, b):
    """have to swap values

    >>> swap_values(10, 20)
    (20, 10)
    """
    a, b = b, a

    ## Bad pattern
    # swap = a
    # a = b
    # b = swap

    print(a, b)

swap_values(10, 20)


def join_strings(lst):
    """
    >>> join_strings(['a', 'b', 'd'])
    abd
    """
    s = ''.join(lst)
    print(s)

    ## Bad pattern
    ## cuz very inefficient
    # s = ''
    # for e in lst:
    #     s += e

join_strings(['a', 'b', 'd'])
