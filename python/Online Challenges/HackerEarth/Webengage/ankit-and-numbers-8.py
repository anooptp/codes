# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 23:04:01 2014

@author: anooptp
"""

import time
start = time.time()


def main():
    import sys
    f = sys.stdin
    f = open("ankit-and-numbers-8.txt")
    
    T = int(f.readline())
    
    for dummy_1 in xrange(T):
        N = int(f.readline())
        ans = 2**(N-1)*sum(xrange(1,N+1))
        print ans

main()

print "Elapsed Time :", time.time() - start

