"""
Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.
"""
def n_copies(_str, n):
    new_str = ""
    if len(_str) >= 2:
        for i in range(n):
            new_str = new_str + _str[:2] + ' '
        print (new_str)
    else:
        for i in range(n):
            new_str = new_str + _str + ' '
        print (new_str)
_str = input('Enter a word to print: ')
n = int(input('Enter the number of times to repeat the word: '))
n_copies(_str, n)
