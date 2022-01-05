#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    New_dictionary = {}
    for i in (a_dictionary.keys()):
        New_dictionary[i] = a_dictionary[i] * 2
    return(New_dictionary)
