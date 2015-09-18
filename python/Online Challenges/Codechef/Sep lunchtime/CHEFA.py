# -*- coding: utf-8 -*-
"""CHEFA
Created on Sun Sep 28 11:53:18 2014

@author: anooptp
"""

import time
start = time.time()


def main():
    import sys

    f = sys.stdin
    f = open("CHEFA.txt")
    
    T = int(f.readline())
    
    for dummy in xrange(T):
        N = int(f.readline())
        A1 = map(int, f.readline().strip().split())
        A1.sort(reverse=True)
        print sum(A1[::2])
    
main()

print "Elapsed Time :", time.time() - start
