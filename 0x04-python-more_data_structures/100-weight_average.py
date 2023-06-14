#!/usr/bin/python3
def weight_average(my_list=[]):
    num = dem = 0
    for element in my_list:
        num += (element[0] * element[1])
        dem += element[1]
    return (num / dem) if dem else 0
