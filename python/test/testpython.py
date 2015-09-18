#!/usr/bin/python
import sys,getopt;

print ("Hello Anoop, Welcome to Python!!!");
if True:
    print("true");
    print ("Answer");
else :
    print("false");
    print ("Answer");

print ('Number of arguments:', len(sys.argv), 'arguments.' )
print ('Argument List:', str(sys.argv))

#getopt.getopt(args, :)

list = ['abc',12,'xyz']

a = 20
b = 20 
c = 0 

if (a is b):
  print("line 1: a & b have same identity");
else :
  print("line 1: a & b do not have same identity");

if (id(a) == id(b)):
  print("line 2: a & b have same identity");
else :
  print("line 2: a & b do not have same identity");

b=30

if (a is b):
  print("line 3: a & b have same identity");
else :
  print("line 3: a & b do not have same identity");

if (a is not b):
  print("line 4: a & b do not have same identity");
else :
  print("line 4: a & b have same identity");

var2 = ''
if var2: 
    print ("2 - Got a true expression value" )
    print (var2 )

print ("Good bye!" )

for letter in 'Python':
   print('Current letter : ',letter);

fruits = ['orange', 'grape', 'banana']

for fruit in fruits:
   print ('fruit name : ',fruit)

for i in range(len(fruits)):
   print ('fruit name : ',fruits[i])