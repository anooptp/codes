# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 13:25:05 2014

@author: anooptp
"""

import time
start = time.time()


def main():
    import sys

    f = sys.stdin
    f = open("Harrenhal.txt")
    
    T = int(f.readline())
    for __ in range(T) :
        s = f.readline()
        if(s==s[::-1]):
            print 1
        else:
            print 2


main()

print "Elapsed Time :", time.time() - start
