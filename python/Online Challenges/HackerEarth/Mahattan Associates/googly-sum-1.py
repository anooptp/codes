# -*- coding: utf-8 -*-
"""
Created on Sat Aug 30 16:21:52 2014

@author: anooptp
"""

"""
In this problem of Googly sum nikki gives you a sequence A consisting of N integers. nikki will call the ith sequence element good if it equals to the sum of some three elements in positions strictly smaller than i . Now nikki asks you a simple question how many good elements does the sequence contain?

Note : An element can be used more than once in the sum i.e lets say sequence is [1 3 5 9] (indexing from 0) consider the following points -

1) In sequence 1 is not good obviously.

2) 3 is good as 1 can be added three times to get 3

3) 5 is good as adding two times 1 and one time 3 will give 5

4) 9 is good as 1+3+5=9 and also adding element 3 three times will give 9 so any of these condition can be used to count 9 as good.

Input :

The first line of input contains the positive integer N , the length of the sequence A. The second line of input contains N space-separated integers representing the sequence A .

Output :

The first and only line of output must contain the number of good elements in the sequence.

Constraints :

1 <= N <= 5000

-10^5 <= Ai <= 10^5
"""


import time
start = time.time()


def main():
    import sys

    f = sys.stdin
    f = open("googly-sum-1.txt")
    
    N = int(f.readline())
    A1 = map(int, f.readline().strip().split())
    
    count = 0
    
    for i in range(1, len(A1)):
        temp_A1 = sorted(A1[:i])
        print temp_A1
    
    
main()

print "Elapsed Time :", time.time() - start
        