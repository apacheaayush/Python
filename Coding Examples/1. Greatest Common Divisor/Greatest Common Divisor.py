# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Basic Algorithm for finding out GCD of two numbers using lists   
   
def gcd(m,n):
    fm = []
    for i in range(1, m+1):
        if (m%i) == 0:
            fm.append(i)
            
    fn = []
    for i in range(1, n+1):
        if (n%i) == 0:
            fn.append(i)
            
    cf = []
    for i in fm:
        if i in fn:
            cf.append(i)
    print("Results from gcd")
    print(cf[-1])
    
gcd(14, 63)
gcd(9999, 100000)
gcd(20000, 35608)


# Do we need three lists?

def gcd1(m, n):
    cf = []
    for i in range(1, min(m,n) + 1): 
        # GCD will always be less than or equal to the smaller number.
        if (m % i) == 0 & (n % i) == 0:
            cf.append(i)
    print("Results from gcd1")
    print(cf[-1])
    
gcd1(14, 63)
gcd1(9999, 100000)
gcd1(20000, 35608)


# Do we need lists at all? Scan Backwards.

def gcd2(m,n):
    print("Results from gcd2")
    for i in range(min(m,n), 1):
        if (m % i) == 0 & (n % i) == 0:
            print(i)
            
gcd2(21, 63)
gcd2(9999, 100000)
gcd2(20000, 35608)
        
