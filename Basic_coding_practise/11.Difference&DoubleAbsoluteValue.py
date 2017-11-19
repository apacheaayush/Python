"""
Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
"""


def diff(x):
    if x - 17 > 0:
        return abs(x - 17) * 2
    else:
        return x - 17

x = int(input('Enter a number: '))
print(diff(x))
