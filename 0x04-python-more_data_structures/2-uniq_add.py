#!/usr/bin/python3
# 2-uniq_add.py

def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    return sum(map(lambda x : int(x), set(my_list)))
