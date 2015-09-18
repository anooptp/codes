# -*- coding: utf-8 -*-
"""
Created on Sat Aug 23 23:10:59 2014

@author: anooptp
"""

import time
start = time.time()


def main():
    import sys

    f = sys.stdin
    f = open("nice-arches-1.txt")
    
    T = int(f.readline())
    
    count = 0
    for dummy_1 in xrange(T):
        word = f.readline().strip()
    
        if word[::-1] == word:
            count += 1
            print word
        else:
            A_pos = 0
            B_pos = 0
            last = None
            bubbly = True
            
            for i in xrange(len(word)):
                if word[i] == 'A':
                    if A_pos != 0:
                        if last == 'A' or B_pos == 0:
                            A_pos = 0
                        else:
                            bubbly = False
                            break
                    else:
                        A_pos = i
                    last = 'A'
                else:
                    if B_pos != 0:
                        if last == 'B' or A_pos == 0:
                            B_pos = 0
                        else:
                            bubbly = False
                            break
                    else:
                        B_pos = i
                    last = 'B'
            if bubbly:
                count += 1
                print word
    print count

    
main()

print "Elapsed Time :", time.time() - start
