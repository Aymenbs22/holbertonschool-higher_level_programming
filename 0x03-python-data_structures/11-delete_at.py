#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if not my_list:
        return
    else:
        my_list.remove(idx)
        return (my_list)
