# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:46:50 2015

@author: anooptp

1.
Mobile Conversations
Max. Marks 100
You have just purchased a new mobile phone and you want to call all of your relatives to brag about your new phone. You have N relatives. You will talk to ith relative for exactly Ti minutes. Each minute costs you 1 dollar . However, your relatives are generous. Hence after the conversation, they will add a recharge of Xi dollars in your mobile. Initially, you have M dollars balance in your mobile phone. 

Find the minimum value of M, that you must have initially, in your phone, so that you don't run out of balance during any of the call (encounter negative balance). 

Note : You can call relatives in any order. Each relative will be called exactly once.

INPUT
The first line will contain N, the number of relatives. Next N lines will have two space separated integers, "Ti Xi" (quotes for clarity), representing call duration with the ith relative and the amount of recharge you will get from that relative after the conversation.

OUTPUT
Output a single integer M, the minimum required initial balance in your mobile phone.

CONSTRAINTS
1 ≤ N,X,T ≤ 105 

Sample Input(Plaintext Link)
 2
1 1
2 1
Sample Output(Plaintext Link)
 2
 
2.
Bruce and the Chocolates
Max. Marks 100
Early this morning, I found our little Bruce sitting on a bench alone in the park. I sat beside him to ask where has he dropped his smile this morning?

Bruce: "Oh, Hi.. I love chocolates. (Who doesn't? ). It's chocolate day in school, and I forgot! Everyone is bringing chocolates. We play a game on this day, where the teacher makes pair of students and the students in each pair share their chocolates. I will have to go empty handed and hence, won't get paired :( "

"That's okay ,Bruce. You can ask your friends to share with you"

Bruce: " I did a smarter thing, I talked to my Mathematics teacher. I'm her favorite! She agreed that I could do the pairing! and from every pair , I could take 'x' number of chocolates, where x is the greatest number of chocolates that divides the number of chocolates with both the students. Now, I don't know how do I pair them! Not everyone can be paired with everyone, friendship issues. Can you help me out?"

You are given the number of chocolates with each student and all the possible pairs of the form (i,j) where ith and jth student can be paired. Help Bruce pair the students, so as to maximize the number of chocolates he can have .

You may assume:

No pairs should overlap. No student is left alone (except Bruce).

Total number of students in class is always odd.

No one is absent on the Chocolate Day!

For a possible pairing (i,j) , ( i+j )mod 2 >0

Input

First line of the input contains T (1<=T<=10) denoting the number of test cases. T testcases follow. For each test case, the first line contains two space-separated integers 'n' (1<=n<200) and 'm' (m>=0) , the total number of students in the class and the number of possible pairings.

Next line contains 'n-1' integers, where Ai (1<=Ai<=10000) is the number of chocolates with the i'th student.

The following m lines contain the description of possible pairs. The k-th line contains two space-separated integers Ik, Jk (1<=Ik,Jk<=n-1 ) .

Output

Output the maximum number of chocolates that Bruce can have.

Sample Input(Plaintext Link)
 2
7 9
1 24 9 18 3 7
1 2
1 4
1 6
3 2
3 4
3 6
5 2
5 4
5 6
5 1
2 7 21 3
1 4
Sample Output(Plaintext Link)
 13
1
Explanation
In the first case, Bruce can make the following pairs of students: - (1,6) and obtain 1 chocolate - ( 3,4) and obtain 9 chocolates - (2,5) and obtain 3 chocolates Hence, 13 chocolates in total

In the second case, Bruce makes the only possible pair: - (1,4) and obtains 1 chocolate.
"""

import time
start = time.time()

def main():
    import sys

    f = sys.stdin
    f = open("mobile_conv.txt")
    
    N = int(f.readline())
    min_amt = 0
    if N==1:
        print map(int, f.readline().split())[0]
        return
        
    #for i in xrange(N-1):
    #    min_amt += reduce(lambda x,y: y-x, map(int, f.readline().split()))
        
    T_X = []
    
    for i in xrange(N-1):
        T_X.append(map(int, f.readline().split()))
        min_amt = min_amt - T_X[-1][0] + T_X[-1][1]
        print min_amt,
    min_amt = min_amt - T_X[-1][0] + T_X[-1][1]
    print T_X
    #min_amt -= map(int, f.readline().split())[0]
    #print abs(min_amt)
    
main()

print "Elapsed Time :", time.time() - start
        