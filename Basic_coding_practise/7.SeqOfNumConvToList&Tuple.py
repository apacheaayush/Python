print('Please enter some numbers below')
x = input('Enter some numbers separated by comma: ')
x = x.split(",")
y = tuple(x)
print('List: ' + str(x))
print('Tuple: ' + str(y))

"""
Splitting a string returns a list
"""
