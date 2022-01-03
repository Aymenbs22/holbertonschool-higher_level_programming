#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    ls = len(my_list)
    for i in range(0, ls):
    print("{:d}".format(my_list[ls - i - 1]))
