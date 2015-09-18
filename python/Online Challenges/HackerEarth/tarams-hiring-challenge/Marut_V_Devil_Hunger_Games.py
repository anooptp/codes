# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:35:15 2015

@author: anooptp
"""

import time
start = time.time()

def alph_count(ac_Arr, word):
    for j in xrange(len(word)):
        ac_Arr[ord(word[j])-97] += 1
        
def main():
    import sys

    f = sys.stdin
    f = open("Marut_V_Devil_Hunger_Games.txt")
    
    score_M, score_D = 0, 0
    
    char_val = map(int, f.readline().strip().split())
    char_count_M = [0 for dummy_i in xrange(26)]
    char_count_D = [0 for dummy_i in xrange(26)]
    
    Q = int(f.readline().strip())
    for i in xrange(Q):
        M = f.readline().strip()
        D = f.readline().strip()
        
        # increment the character count for Marut
        alph_count(char_count_M, M)
            
        # increment the character count for Devil
        alph_count(char_count_D, D)
            
    score_M = reduce(lambda x, y: x + y, map(lambda x, y: x * y , char_val, char_count_M))
    score_D = reduce(lambda x, y: x + y, map(lambda x, y: x * y , char_val, char_count_D))
    
    print score_D, score_M
    
    if score_D > score_M:
        print "Devil"
    elif score_M > score_D:
        print "Marut"
    else:
        print "Draw"
        
    
main()

print "Elapsed Time :", time.time() - start
