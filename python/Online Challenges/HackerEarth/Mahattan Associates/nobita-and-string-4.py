# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 16:11:20 2014

@author: anooptp
"""

import time
start = time.time()


def main():
    import sys

    f = sys.stdin
    f = open("nobita-and-string-4.txt")
    
    T = int(f.readline())
    for dummy in xrange(T):
        wrd = f.readline().strip().split()
        
        print ' '.join(wrd[::-1])
    
    
main()

print "Elapsed Time :", time.time() - start
        