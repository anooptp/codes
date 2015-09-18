# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 12:36:52 2015

@author: anooptp
"""

import time
start = time.time()

"""
def matrix(n):
    mat = [[] for i in xrange(n)]
    
    for i in xrange(n):
        for j in xrange(n):
            mat[i].append(i^j)
    print mat[n-1]
    mat_max = 0
    mat_max_count = 0
    dummy_i, dummy_j = 0, 0
    for i in xrange(n):
        for j in xrange(n):
            if mat[i][j] == mat_max:
                mat_max_count += 1
            if mat[i][j] > mat_max:
                mat_max_count = 1
                mat_max = mat[i][j]
                dummy_i, dummy_j = i, j
    print n, mat_max, mat_max_count
    print 
    

for i in xrange(20,40):
    matrix(i)

"""

def main():
    import sys
    import math
    
    f = sys.stdin
    f = open("royMaximumXOR.txt")
    
    T = int(f.readline())
    for dummy_i in range(T):
        N = int(f.readline())
        if N==1:
            print 0, 1
        else:
            print int(2**math.ceil(math.log(N, 2))-1),

            if (N-2**math.floor(math.log(N, 2))) == 0:
                print int(2 * (2**math.floor(math.log(N, 2))- 2**math.floor(math.log(N-1, 2))))
            else:
                print int(2 * (N-2**math.floor(math.log(N, 2))))
    
main()

print "Elapsed Time :", time.time() - start
