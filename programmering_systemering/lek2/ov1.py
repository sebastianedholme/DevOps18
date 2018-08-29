# coding=utf-8 
import os
import random
import sys

for i in range(10):
    print(i)

print("\nI can now make loops")


# If satser
#x = 30
#
#if x < 30:
    #print('\nstämmer')
#else:
    #print('\nnope')

y = 40

# Hur man kan formatera strängar för att skriva ut heltal med strängar.
if y != 40:
    print "{} {}".format("y is:",y) 
    print("and not 40") 
else:
    print "{} {}".format("y is:",y) 
    print("is 40")

x = 5
y = 10

if x + y == 15:
    print('true')


x = random.randrange(0, 100)
print(x)
