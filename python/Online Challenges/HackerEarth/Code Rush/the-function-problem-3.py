# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 15:45:35 2014

@author: anooptp
"""

import time
start = time.time()

FIB ={0 : 1}

def fibonacci(num):
    "O(log(n)) implementation of fibonacci using fast doubling."
    if num >= 0:
        return fib_helper(num)[0]

def fib_helper(num):
    "Helper function for fibonacci()."
    if num == 0:
        return (0, 1)
    elif num == 1:
        return (1, 1)
    else:
        f_k, f_k_1 = fib_helper(num // 2)
        f_k_even = f_k * (2 * f_k_1 - f_k)
        f_k_odd = f_k_1 * f_k_1 + f_k * f_k
        return (f_k_even, f_k_odd) if num % 2 == 0 else (f_k_odd, f_k_even +
                f_k_odd)
        
def fib(n):
    recepie = bin(n)[3:]
    v1, v2, v3 = 1, 1, 0
    for rec in recepie:
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, v1*v2+v2*v3, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2
     
def main():
    import sys
    
    f = sys.stdin
    f = open("the-function-problem-3.txt")
    
    T = int(f.readline())
    A1 = map(int, f.readlines())
    
    MOD = 1000000007
    
    for i in A1:
        res = fib(i+2)
        print i, res%MOD
    
main()

print "Elapsed Time :", time.time() - start
