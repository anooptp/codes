# -*- coding: utf-8 -*-
"""
Created on Sat Aug 02 17:33:04 2014

@author: anooptp
"""

import time
start = time.time()

class Node():
    def __init__(name):
        self.name = name
        self.leaves = []
        
    def __str__(name):
        return self.name, " : ",self.leaves

    
def main():
    import sys

    f = sys.stdin
    f = open("big-p-and-party-1.txt")
    
    A, B = map(int,f.readline().split())
    
    luckiness = [0 for i in range(A)]
    dance_arr = []
    for d_pair in f.readlines():
        print map(int, d_pair.split())
    
    print dance_arr
    
main()
        
print "Elapsed Time :", time.time() - start