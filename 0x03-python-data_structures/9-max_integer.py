#!/usr/bin/python3
'''get the biggest integer of a list'''
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    biggest_int = 0
    for i in range(len(my_list)):
        if my_list[i] > biggest_int:
            biggest_int = my_list[i]
        continue
    return biggest_int
