#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    n = 0
    for item in my_list:
        try:
            if n < x:
                print("{}".format(item), end="")
                n += 1
        except:
            break
    print()
    return n
