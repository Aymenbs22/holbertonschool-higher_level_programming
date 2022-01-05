#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    elif a_dictionary:
        Big = max(a_dictionary, key=lambda x: a_dictionary[x])
        return (Big)
    else:
        return(None)
