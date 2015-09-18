# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 17:32:14 2014

@author: anooptp
"""


import time
start = time.time()

def cal_magic(sA1, mag_dict):
    prime_digits = ['2','3','5','7']
    count = 0
    j = 2
    k = 0
    max_num = sA1[-1]
    
    while(j <= max_num):
        s = str(j)
        n_inc = True
        if s.count('2') or s.count('3') or s.count('5') or s.count('7'):
            for i in xrange(len(s)):
                if s[i] in prime_digits and (j + 10**len(s[i+1:])) < sA1[k]:
                    count += 10**len(s[i+1:])
                    j += 10**len(s[i+1:])
                    n_inc = False
                    break
                elif s[i] in prime_digits:
                    count += 1
                    break
        if n_inc:
            if j == sA1[k]:
                k += 1
                mag_dict[j] = count
            j += 1
            

def main():
    import sys
    
    f = sys.stdin
    f = open("aaryan-and-the-magical-numbers-2.txt")
    
    T = int(f.readline())
    
    A1 = map(int, f.readlines())
    sort_A1 = sorted(A1)
    magic_dict = {}
    
    cal_magic(sort_A1, magic_dict)
    
    for i in A1:
        print magic_dict[i]
    
main()

print "Elapsed Time :", time.time() - start
