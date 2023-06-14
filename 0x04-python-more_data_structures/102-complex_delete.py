#!/usr/bin/python3
def complex_delete(my_dict, value):
    return {key: val for key, val in my_dict.items() if val != value}
