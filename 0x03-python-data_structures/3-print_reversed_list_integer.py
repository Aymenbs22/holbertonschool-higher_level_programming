#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    else:
        j = len(my_list)
        for i in range(0, j):
            print("{:d}".format(my_list[j - i - 1]))
