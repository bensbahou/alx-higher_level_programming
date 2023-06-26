#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for item in my_list:
        try:
            print("{:d}".format(item), end="")
            i += 1
        except (ValueError, TypeError):
            continue
    print()
    return i
