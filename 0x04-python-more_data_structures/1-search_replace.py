#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return
    new_list = my_list[0:100]
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    return(new_list)
