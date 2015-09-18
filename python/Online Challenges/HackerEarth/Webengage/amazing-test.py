# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 23:37:19 2014

@author: anooptp
"""

import time
start = time.time()


def main():
    import sys

    f = sys.stdin
    f = open("amazing-test.txt")
    
    T = int(f.readline())
    
    for dummy in xrange(T):
        n, x = map(int, f.readline().strip().split())
        A1 = map(int, f.readline().strip().split())
        A1.sort()
        print A1
        if n >= 2:
            x -= float(sum(A1[:-2]))/2
            print x
            if A1[-1] > x or A1[-2] > x:
                print "NO"
            else:
                print "YES"
        else:
            if A1[0] > x:
                print "NO"
            else:
                print "YES"
    
main()

print "Elapsed Time :", time.time() - start
