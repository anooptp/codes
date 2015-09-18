# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 21:53:34 2014

@author: anooptp
"""

import time
import sys

start = time.time()
f=sys.stdin
f = open("input10.txt")

T = int(f.readline())
assert(1<= T <= 6)

for dummy in xrange(T):
    numN, numQ = map(int, f.readline().split())
    
    assert(1 <= numN <= 100000)
    assert(1 <= numQ <= 50000)
    
    A = map(int, f.readline().split())
    
    questions = []
    
    
    for i in xrange(numQ):
        X, l, r = map(int, f.readline().split())
        high = -1000000
        for j in A[l-1:r]:
            xor = j^X
            if xor > high:
                high = xor
        print high
        
print "Elapsed Time :", time.time() - start