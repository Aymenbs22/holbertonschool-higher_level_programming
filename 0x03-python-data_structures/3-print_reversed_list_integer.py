#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    l = len(my_list)
    for i in range(0, l):
        print("{:d}".format(my_list[l - i - 1]))
