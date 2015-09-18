# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 21:58:40 2014

@author: anooptp
"""
import time

start = time.time()

N = int(raw_input())
assert(1<= N <= 10**6)

A = map(int, raw_input().split())

numQ = int(raw_input())
assert(1 <= numQ <= 50000)

questions = []

for i in range(numQ):
    quest = raw_input().split()
    l = int(quest[0])
    r = int(quest[1])
    X = int(quest[2])
    temp ={}
    low = 10**9
    for j in A[l-1:r]:
        xor = j^X
        if xor <= low:
            if xor not in temp:
                temp[xor] = [j, 1]
                low = xor
            else:
                temp[xor][1] += 1                
    print temp[low][0], temp[low][1]
    
print "Elaspsed time :", time.time() - start
#### Sample Input
#7
#1 3 2 3 4 5 5
#5
#1 1 1
#1 2 2
#1 4 3
#1 5 4
#1 7 5
#
#### Sample Output
#1 1
#3 1
#3 2
#4 1
#5 2
