# -*- coding: utf-8 -*-
"""
Created on Sun Aug 03 23:59:50 2014

@author: anooptp
"""


import time
start = time.time()


def gcd(m, n):
    while(n!=0):
        r = m%n
        m = n
        n = r
    return m
        

def main():
    import sys

    f = sys.stdin
    f = open("gcd-recruit.txt")
    
    N = int(f.readline())
    
#    A = [0 for x in xrange(3001)]
    A = [0] * 3001
    #A1 = map(int, f.readlines())
    
    for i in xrange(N):
        A[int(f.readline())] += 1
    #for i in A1:
    #    A[i] += 1
    
    ans = 0
    for i in xrange(2, 3001):
        count = 0
        if A[i] > 0:
            for j in xrange(i+1, 3001):
                if A[j] > 0 and gcd(i, j) > 1:
                    count += A[j]
            ans += A[i] * count
            ans += (A[i] * (A[i] - 1)) / 2
    print ans
    
main()

print "Elapsed Time :", time.time() - start
        