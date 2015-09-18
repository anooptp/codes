# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 23:43:20 2014

@author: anooptp
"""

import time
start = time.time()


def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
    
    
def main():
    import sys

    f = sys.stdin
    f = open("small-factorials.txt")
    
    T = int(f.readline())
    
    arr_N = map(int, f.readlines())
    
    for n in arr_N:
        print fact(n)
    
main()

print "Elapsed Time :", time.time() - start

## Expected Output
#1
#2
#120
#6