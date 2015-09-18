# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 15:18:18 2014

@author: anooptp
"""


import time
start = time.time()


def get_prime(n):
    """ Input n>=6, Returns a list of primes, 2 <= p < n """
    correction = (n%6>1)
    n = {0:n,1:n-1,2:n+4,3:n+3,4:n+2,5:n+1}[n%6]
    sieve = [True] * (n/3)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
      if sieve[i]:
        k=3*i+1|1
        sieve[      ((k*k)/3)      ::2*k]=[False]*((n/6-(k*k)/6-1)/k+1)
        sieve[(k*k+4*k-2*k*(i&1))/3::2*k]=[False]*((n/6-(k*k+4*k-2*k*(i&1))/6-1)/k+1)
    return ['2','3'] + [str(3*i+1|1) for i in xrange(1,n/3-correction) if sieve[i]]


def main():
    import sys

    f = sys.stdin
    f = open("the-xperiment.txt")
    
    T = int(f.readline())
    prime_num = get_prime(48618)
    prime_num = prime_num + ['0']* (79000-5000)
    A1 = map(int, f.readlines())
    
    ans = []
    for i in xrange(T):
        if A1[i]==1:    
#            print '1'
            ans.append(float(1) / 10**6)
        else:
#            print ' '.join(prime_num[:A1[i]])
            ans.append(float(sum(map(int, prime_num[:A1[i]])))/ 10**6)
    print ans
    print sum(ans)
    
    
main()

print "Elapsed Time :", time.time() - start
