# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 11:00:47 2015

@author: anooptp
"""

import time
start = time.time()

def main():
    import sys
    
    f = sys.stdin
    f = open("royCountingSortedSubstrings.txt")
    
    T = int(f.readline())
    assert(1 <= T <= 10)
    for dummy_i in range(T):
        N = int(f.readline())
        S = f.readline()[:N]
        
        #print N, S
        total_sub = 0
        count = 1
        for i in xrange(1,N):
            if S[i-1] <= S[i]:
                count += 1
            else:
                total_sub += ((count * (count + 1)) / 2) - count
                count = 1
            #print S[i-1], S[i], count, total_sub
            
        if count > 1:
            total_sub += ((count * (count + 1)) / 2) - count
        #print count, total_sub
        total_sub += N
        print total_sub
    
main()

print "Elapsed Time :", time.time() - start
