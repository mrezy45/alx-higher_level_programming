#!/usr/bin/python3
# 0-add_integer.py
'''function that adds 2 integers.'''


def add_integer(a, b=98):
    '''a function that adds 2 integers.

    a and b must be first casted to integers if they are float.
    a and b must be integers or floats, otherwise raise a TypeError
    exception with the message a must be an integer
    or b must be an integer

    Returns an integer: the addition of a and b.
    '''

    if (not isinstance(a, int) and not isinstance(a, float)):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
