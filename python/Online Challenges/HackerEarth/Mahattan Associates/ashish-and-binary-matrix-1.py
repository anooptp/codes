# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 16:45:08 2014

@author: anooptp
"""

import time
start = time.time()


def main():
    import sys

    f = sys.stdin
    f = open("ashish-and-binary-matrix-1.txt")
    
    T = int(f.readline())
    
    for dummy_i in xrange(T):
        N, M = map(int, f.readline().strip().split())
        bin_flag = False
        
        mat = []
        for dummy_j in xrange(N):
            mat.append(f.readline().strip())
            
        for i in xrange(M):
            temp_mat = [wrd[:i]+wrd[i+1:] for wrd in mat]
            if len(set(temp_mat)) == N:
                bin_flag = True
                break
        if bin_flag:
            print "Yes"
        else:
            print "No"
    
    
main()

print "Elapsed Time :", time.time() - start
        