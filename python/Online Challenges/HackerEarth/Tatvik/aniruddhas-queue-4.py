# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 22:15:36 2014

@author: anooptp
"""

import time
start = time.time()


def main():
    import sys

    f = sys.stdin
    f = open("aniruddhas-queue-4.txt")
    
    T = int(f.readline())
    
    for dummy_1 in xrange(T):
        N = int(f.readline())
        X = map(int, f.readline().strip().split())
        M = int(f.readline())
        X_sum = sum(X)
        rem = M - (X_sum * (M / X_sum))
        ans = 0
        if M == 0:
            print 0
        elif rem == 0:
            i = N
            while i > 0:
                if X[i-1] != 0:
                    print i
                    break
                i -= 1
        else:
            i = 1
            while i <= N:
                ans += X[i-1]
                if ans >= rem:
                    print i
                    break
                i += 1

    
main()

print "Elapsed Time :", time.time() - start

#1
#3