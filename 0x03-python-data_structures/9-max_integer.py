#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max_int = my_list[0]
    for element in my_list[1:]:
        if element > max_int:
            max_int = element
    return max_int
