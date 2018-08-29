# coding=utf-8 
import os
import random
import sys

##### Öv1 och Öv2.
myNumber = 10

if myNumber > 10:
    print('Huuuge')
elif myNumber < 1:
    print('Not that small')
else:
    print('Under 10 eller över 10')


###### Öv3.
x = 10
y = 20

if x > 10 and y < 15:
    print(y+x) # just for fun
###### Öv4.

for i in range(10):
    print(i)

##### Öv5.
x = 110

## Get x to 0 with two loops
for i in range(0, 10):
    x -= 1
    print(x)
    for i in range(0, 10):
        x -= 1
        print(x)

###### Andra lektionsuppgifter
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
    print("{} {}".format("y is:",y))
else:
    print("{} {}".format("y is:",y))
    print("is 40")

x = 5
y = 10

if x + y == 15:
    print('true')


x = random.randrange(0, 100)
print(x)
