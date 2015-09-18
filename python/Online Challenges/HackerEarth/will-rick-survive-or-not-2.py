# -*- coding: utf-8 -*-
"""
Created on Sat Aug 02 14:41:27 2014

@author: anooptp
"""

import time
start = time.time()


def check_flag(A, mv_sum):
    if A:
        return A[0]-mv_sum == 0
    return False
    
def main():
    import sys

    f = sys.stdin
    f = open("will-rick-survive-or-not-2.txt")
        
    T = int(f.readline())
    
    for dummy in xrange(T):
        numN = int(f.readline().strip())
        
        A = map(int, f.readline().strip().split())
        
        bullet_count = 6
        move_sum = 0
        A.sort()
        
        rick_flag = False
        while A and not rick_flag:
            if bullet_count < 1:
                move_sum += 1
                rick_flag = check_flag(A, move_sum)
                
                bullet_count = 6
            else:
                move_sum += 1
                A.pop(0)
                rick_flag = check_flag(A, move_sum)
                bullet_count -= 1
        if rick_flag:
            print "Goodbye Rick"
            print numN - len(A)
        else:
            print "Rick now go and save Carl and Judas"

main()
        
print "Elapsed Time :", time.time() - start