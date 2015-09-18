# -*- coding: utf-8 -*-
"""
Created on Sun Aug 10 23:59:50 2014

@author: anooptp
"""


import time
start = time.time()


def main():
    import sys

    f = sys.stdin
    f = open("find-mode.txt")
    
    T = int(f.readline())
    
    for i in xrange(T):
        N = int(f.readline())
        A = map(int, f.readline().strip().split())
        
        dic = {}
        for i in A:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        maximum = max(dic.values())
        
        li =[]
        for key in dic:
            if dic[key] == maximum:
                li.append(int(key))
        
        li.sort(reverse = True)
        s = ''
        for i in li:
            s += str(i)+" "
        print s
    
main()

print "Elapsed Time :", time.time() - start


## Expected Output
#2 
#3 2 