#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    result = 0
    for x in set(my_list):
        result += x
    return (result)

"""
Write a function that adds all unique integers in a list (only once for each integer).

Prototype: def uniq_add(my_list=[]):
You are not allowed to import any module
"""
