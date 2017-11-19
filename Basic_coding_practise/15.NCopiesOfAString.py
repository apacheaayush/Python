"""
Write a Python program to get a string which is n (non-negative integer) copies of a given string.
"""

def larger_string(_str, n):
    new_str = ""
    for i in range (0, n):
        new_str = new_str + _str + ' '
    return new_str

print(larger_string('abc', 2))
