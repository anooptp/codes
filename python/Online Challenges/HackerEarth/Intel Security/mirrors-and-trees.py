# -*- coding: utf-8 -*-
"""
Created on Fri Sep 19 23:21:51 2014

@author: anooptp
"""


import time
start = time.time()


def main():
    import sys, math

    f = sys.stdin
    f = open("mirrors-and-trees.txt")
    
    T = int(f.readline())
    powers = [2**i for i in range(19)]
    node_range = [int(sum(powers[:i])) for i in range(len(powers))]
    for dummy_1 in xrange(T):
        N = int(f.readline())
        A1 = map(int, f.readline().strip().split())
        level = int(math.log(N+1, 2))
        rec = []
        for i in xrange(1, level+1):
            ind = False
            for j in xrange(node_range[i+1]-1,node_range[i]-1, -1):
                if A1[j] != 0:
                    rec.append([A1[j]])
                    ind = True
                    break
            if ind == False:
                break
            for k in xrange(node_range[i],node_range[i+1]):
                if A1[k] != 0:
                    if A1[k] != rec[i-1][0]:
                        rec[i-1].append(A1[k])
                    break
        print A1[0]
        for i in rec:
            print i[0]
        for j in rec:
            if len(j)==2:
                print j[1]
        print 


main()

print "Elapsed Time :", time.time() - start


## Expected Output
#1
#3
#2
#
#1
#3
