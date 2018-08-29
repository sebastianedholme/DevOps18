import random
import math

x = random.randrange(0, 101)

for i in range(x, 101):
    print(i)

for i in range(0, 1000):
    x = random.randrange(0, 101)
    if x > 99:
        print(x)

for i in range(20):
    print(i)

print('----------------------------------------------------------------')

y = 0
slumptal = random.randrange(0,100)

while slumptal > 20:
    y += 1
    slumptal = random.randrange(0, 100)
    print (y, slumptal)

print('----------------------------------------------------------------')

while random.randrange(0, 100) == 20: break

i=0

while (random.randrange(0, 100) != 20) or print(i): i+=1
