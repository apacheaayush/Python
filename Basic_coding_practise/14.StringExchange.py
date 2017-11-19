"""
Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.
"""
def str_change(_str):
    if len(_str) >= 2 and _str[:2] == 'Is':
        return _str
    else:
        return 'Is' + _str
    
_str = input('Enter a word: ')

print(str_change(_str))
