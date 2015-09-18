# -*- coding: utf-8 -*-
"""
Created on Sun Aug 17 15:15:13 2014

@author: anooptp
"""


import time
start = time.time()


#def factors(n):    
#    return set(reduce(list.__add__, 
#                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#def factors(n):
#    return set(x for tup in ([i, n//i] 
#                for i in range(1, int(n**0.5)+1) if n % i == 0) for x in tup)    

import itertools
flatten_iter = itertools.chain.from_iterable
def factors(n):
    return set(flatten_iter((i, n//i) 
                for i in range(1, int(n**0.5)+1) if n % i == 0))
                
def main():
    import sys
    
    f = sys.stdin
    f = open("coin-group-2.txt")
    
    T = int(f.readline())
    A1 = map(int, f.readlines())
    
    for i in xrange(T):
        print len(factors(A1[i]))
    
    
main()

print "Elapsed Time :", time.time() - start
