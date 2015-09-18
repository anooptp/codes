# -*- coding: utf-8 -*-
"""
Created on Sun Sep 28 22:40:06 2014

@author: anooptp
"""

import time
start = time.time()

def main():
    import sys

    f = sys.stdin
    f = open("roy-and-trending-topics-1.txt")
    
    N = int(f.readline())
    d1 = {}
    d2 = {}
    for dummy in xrange(N):
        _id, cur_z, p, l, c, s = map(int, f.readline().strip().split())
        new_z = (50*p) + (5*l) + (10*c) + (20*s)
        if _id not in d1:
            d1[_id]=new_z
            d2[_id]= new_z - cur_z
    a=sorted(d2.items(), key=lambda x: (x[1], x[0]), reverse=True)[:5]
    for i in xrange(len(a)):
        print "%s %s" % (a[i][0], d1[a[i][0]])
        
    
main()

print "Elapsed Time :", time.time() - start
