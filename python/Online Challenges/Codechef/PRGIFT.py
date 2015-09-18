# -*- coding: utf-8 -*-
"""
Created on Sat Aug 02 12:17:49 2014

@author: anooptp
"""

import time
start = time.time()

import sys

f = sys.stdin
f = open("PRGIFT.txt")

T = int(f.readline())

for dummy in xrange(T):
    numN, numK = map(int, f.readline().split())
    #assert(1 <= numN <= 50)
    #assert(0 <= numK <= numN)
    
    A = map(int, f.readline().strip().split())
    
    count = 0
    gift_flag = numK == 0
    for i in xrange(numN):
        if not gift_flag:
            if A[i]%2 == 0:
                count += 1
                if count == numK:
                    gift_flag = True
            elif count > 0:
                gift_flag = False
                break
        else:
            if A[i] % 2 == 0:
                gift_flag = False
                break
    if gift_flag:
        print "YES"
    else:
        print "NO"
#    for i in xrange(numN):
#        if A[i]%2 == 0:
#            if count > 0:
#                count += 1
#                if count == numK:
#                    if i != numN-1 and A[i+1]%2==0:
#                        print "NO"
#                        break
#                    else:
#                        print "YES"
#                        break
#            else:
#                count += 1
#                if count == numK:
#                    if i != numN-1 and A[i+1]%2==0:
#                        print "NO"
#                        break
#                    else:
#                        print "YES"
#                        break
#        else:
#            if count > 0:
#                print "NO"
#                break
            
print "Elapsed Time :", time.time() - start
