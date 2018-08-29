# coding=utf-8

""" hej
Nu kan jag
göra
det
här
"""


import sys
import os
import random

# Lagra mitt namn
name = "Sebastian"

# Skriv ut mitt namn
print("Hej " + name)

# Jag kör \ som escape character framför " för att skriva ut den utan att python ska
# ska förstå den som jag vill. 
print("Hej Nackademin \"i solna\"")
print ('Hej Nackademin "i solna')

# skriv \ behövs inte två \\, men när jag skriver ut två så får jag ändå ut bara 1. Så escape character fungerar fortfarande.
print("Nackademin i \\ solna")

# Nu ska vi göra några uträkningar med hjälp av variablar och olika matematiska operander
x = 5
y = x - 1
z = x + y

#  båda utrycken ger samma resultat
tal -= 5
tal = tal - 5

# skriv ut tal
print(tal)

#print(tal - 5)
#print(z)
#
## Göra beräkningar direkt i print
#print(z*x)

# Order of operations
xy = (1 + 2 - 10) * 4

print(xy)

print(5**10)

# Skriv ut
complexity = (1 + 10 - 2) / 2 ** 2
print(complexity)
