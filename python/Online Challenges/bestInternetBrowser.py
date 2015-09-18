# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 19:29:57 2014

@author: anooptp
"""
import re
import time

start = time.time()
num = int(raw_input())

assert(1 <= num <= 100)

websites = []

for dummy in range(num):
    websites.append(raw_input())
    assert(1 <= len(websites[-1]) <= 200)
    
for web in websites:
    word = web[4:-4]
    word = re.sub('[aeiouAEIOU]','', word)
    print str(len(word) + 4)+"/"+str(len(web))
    
print "Elapsed Time :", time.time() - start, "ms"
#######Input
#2
#www.google.com
#www.hackerearth.com
