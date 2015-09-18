# -*- coding: utf-8 -*-
"""
Created on Sun Aug 24 00:22:19 2014

@author: anooptp
"""


import time
start = time.time()


def fast_power(a,n):
    result = 1
    power = n
    base = a
    while power > 0:
        if (power & 1) == 1:
            result = result * base
        power = power >> 1
        base *= base
    return result

def main():
    import sys

    f = sys.stdin
    f = open("quantum-and-divisibility-2.txt")
    
    T = int(f.readline())
    
    for dummy_1 in xrange(T):
        a, b, c , d = map(int, f.readline().strip().split())
        if fast_power(a, b) % fast_power(c, d) == 0:
            print "Divisible"
        else:
            print "Not divisible"

    
main()

print "Elapsed Time :", time.time() - start
