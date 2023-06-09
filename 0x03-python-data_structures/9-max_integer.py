#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        large = my_list[0]
        for num in my_list[1:]:
            if large < num:
                large = num
        return large
    return None
