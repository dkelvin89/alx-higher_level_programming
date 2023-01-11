#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    """Delete keys with a specific value in a dictionary."""
    while value in a_dictionary.values():
        for k, v in a_dictionary.items():
            if v == value:
                del a_dictionary[k]
                break

    return (a_dictionary)

"""
Write a function that deletes keys with a specific value in a dictionary.

Prototype: def complex_delete(a_dictionary, value):
If the value doesn’t exist, the dictionary won’t change
All keys having the searched value have to be deleted
You are not allowed to import any module
"""
