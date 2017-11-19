"""
Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum. 
"""

def sum_three(a, b, c):
    if a == b == c:
        return 3 * a
    else:
        return (a + b + c)
    
print(sum_three(13, 13, 13))
print(sum_three(13, 15, 17))
