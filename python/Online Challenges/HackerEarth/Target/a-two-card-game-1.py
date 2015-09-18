# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 21:33:09 2014

@author: anooptp
"""

import time
start = time.time()


def main():
    import sys

    f = sys.stdin
    f = open("a-two-card-game-1.txt")
    
    N = int(f.readline())
    A1 = map(int, f.readline().strip().split())
    if N <= 0:
        print '0.000000 0.000000'
    elif N == 1:
        print '1.000000 1.000000'
    elif N>=2:
        A2 = sorted(A1[:N], reverse=True)
        if A2[1] == A2[0]:
            print '0.000000 0.000000'
        else:
            print '0.500000 0.500000'
            
    
main()

print "Elapsed Time :", time.time() - start
