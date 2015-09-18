# -*- coding: utf-8 -*-
"""palindromic-numbers-7
Created on Fri Aug 08 21:31:35 2014

@author: anooptp
"""

import time
start = time.time()

def isPalindrome(s):
    m = len(s)
    pal = True
    for i in xrange(m/2):
        if s[i] != s[-i-1]:
            pal =False
            break
    return pal
    

def main():
    import sys

    f = sys.stdin
    f = open("palindromic-numbers-7.txt")
    
    T = int(f.readline())
    
    for i in xrange(T):
        A, B = map(int, f.readline().strip().split())
        count = 0
        for j in xrange(A, B+1):
            if isPalindrome(str(j)):
                count += 1
        print count
            
main()


print "Elapsed Time :", time.time() - start
        