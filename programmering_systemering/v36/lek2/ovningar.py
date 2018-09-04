# coding=utf=8
import operator
# Skapa listor med for loop
x = [0 ,223, "hej", "adam", 33]
x = [i for i in range(4, 10)]
print(x)

# skapa lista beroende på beroe på är större eller lika med 4

x = [ i for i in range(10) if i >= 4]
print(x)

# Dictionary för räkning
u = {"*": operator.mul, "+": operator.add, "-": operator.sub, "%": operator.mod, "**": operator.pow}
x = [ i for i in range(10) if u["%"](i,2)==0]
print(x)

# Modulus 
x = [i for i in range(100) if not (i%3==0 or i%5==0)]
print(x)

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x = [i for i in x if i > 4]
print(x[-1:])
print(x[-1]) # tar man bort kolonen får jag ut elementet i det objekt det är. med kolon får du ut den som lista
print(x[2:6])
y = x[2:6]
print("y: {}".format(y))


# Lista med element som är produkten*2
x = [i*2 for i in range(10)]
print(x)
del x

print("-----------------------------------------------------------------------------------")
x = [ i for i in range(10) ]
print(x)

x = []

print("-----------------------------------------------------------------------------------")
while len(x)<10: x.append(len(x)*2)
print(x)
print("-----------------------------------------------------------------------------------")

x = "Hej här en lång sträng, som är sjukt trevlig."

print(x[-3:])

# Ett knepigt sätt
x = [x[i:i+1] for i in range(len(x))]
print(x)

x = [ i.capitalize() for i in x]
print(x)

print("-----------------------------------------------------------------------------------")

x = "Hejhärenlångsträngsomärsjukttrevlig"

print(x.partition("lång"))
print(x.partition("Hej"))
print(x.split("Hej"))
print("jjjjjjjHej hasdf jjjjjjjjjjasjdjjjsadfjasjjjj".strip('j'))
print("-".join(["hej", "på", "dig"]))
