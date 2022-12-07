#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    average = 0
    size = 0
    for element in my_list:
        average += (element[0] * element[1])
        size += element[1]
    return average / size
