#!/usr/bin/python3
def complex_delete(my_dict, value):
    for key, val in list(my_dict.items()):
        if val == value:
            del my_dict[key]
    return my_dict
