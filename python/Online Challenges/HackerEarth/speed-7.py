# -*- coding: utf-8 -*-
"""
Created on Thu Aug 07 23:25:57 2014

@author: anooptp
"""


import time
start = time.time()


def main():
    import sys

    f = sys.stdin
    f = open("speed-7.txt")
        
    T = int(f.readline())
    
    for i in xrange(T):
        N = int(f.readline())
        A = map(int, f.readline().strip().split())
        low = A[0]
        count = 1
        for j in A[1:]:
            if j <= low:
                count += 1
                low = j
        print count
    
main()
        
print "Elapsed Time :", time.time() - start
