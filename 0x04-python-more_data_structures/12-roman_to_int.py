#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    decs = [roman_dict[x] for x in roman_string]
    output = 0
    for i, dec in enumerate(decs):
        output += dec
        if i > 0 and dec > decs[i - 1]:
            output -= 2 * decs[i - 1]
    return output
