#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = map(lambda i: replace if i == search else i, my_list)
    return (list(result))

"""
Write a function that replaces all occurrences of an element by another in a new list.

Prototype: def search_replace(my_list, search, replace):
my_list is the initial list
search is the element to replace in the list
replace is the new element
You are not allowed to import any module
"""
