# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 23:30:41 2014

@author: anooptp
"""

import time
start = time.time()

def prod(li):
    r = 1
    for x in li:
        r *= x
    return r

def main():
    import sys
    
    f = sys.stdin
    f = open("a-to-b-1.txt")
    
    N = int(f.readline())
    A = map(int, f.readline().strip().split())
    Q = int(f.readline())
    i = 0
    prd = prod(A)
    while i < Q:
        i += 1
        temp = map(int, f.readline().strip().split())
        print temp
        if temp[0] == 0 and len(temp) == 3:
            if A[temp[1]-1] != 0 and temp[2]!=0:
                prd = int(float(prd) / A[temp[1]-1] * temp[2])
            elif temp[2]!=0:
                prd = int(float(prd) * temp[2])
            A[temp[1]-1] = temp[2]
        elif temp[0] == 1  and len(temp) == 2:
            #prd = reduce(lambda x, y: x * y, A)
            #prd = reduce(mul, A)
            if A[temp[1]-1] != 0:
                print int(float(prd)/A[temp[1]-1])
    
    
main()

print "Elapsed Time :", time.time() - start
