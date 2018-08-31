# coding=utf-8
import os
import random
import sys

# Some for loops

staticNumber = 5

print("-----------------------------------")
print("--------GÅNGER TABELL--------------")
for i in range(0, 11):
    answer = staticNumber * i
    print(staticNumber, " * ", i, " = ", answer)

print("-----------------------------------")
print("--------GÅNGER TABELL REV----------")
for i in range(10,-1,-1):
    answer = staticNumber * i
    print(staticNumber, " * ", i, " = ", answer)

print("-----------------------------------")
print("--------EXPONENSIELLA FUNKTIONER---")
for i in range(11):
    answer = i**i
    print(i, "^", i, " = ", answer)

print("-----------------------------------")
print("--------TABELL --------------------")

for i in range(3):
    for i in range(4):
        print("*", end="")
    print()

print("-----------------------------------")
print("--------TABELL MED WHILE-----------")
colum = 5
row = 3
x = 0
y = 0

while x <= colum:
    x += 1
    while y <= row:
        y += 1
        print("*", end=" ")
    print()
    y = 0

print("--------TABELL MED WHILE-----------")
for i in range(3):
    for i in range(4):
        print("|", end="")
        print("*", end="")
    print("|")

print("---------------BYTA VÄRDEN---------")
x = 10
y = 20

z = x
x = y
y = z

print(x,y)

print("-------BYTA VÄRDEN ONELINE---------")
x = 10
y = 20

x, y = y, x

print(x,y)

print("-----------------------------------")
print("--------MASTRIS--------------------")

for i in range(3):
    for j in range(3):
        print(i**4, " ", end="")
    print()


print("Vad är ditt förnamn?", end="")
name = sys.stdin.readline()
print("Hej", name)

print("Vad är ditt förnamn? ", end="")
name = input()
print("Hej {}!".format(name))
