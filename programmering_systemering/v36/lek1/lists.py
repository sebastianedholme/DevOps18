names = ["Olof","Patrik","Sven"]
numbers = [ 123,3213,241]

print(names[2])
print(names[1])
names[1] = "Another"
print(names[1])
print(names)

for i in range(len(names)):
    names[i] = ""

print(names)

names = ["Olof","Patrik","Sven", "Carl"]

for i in names:
    print(i)

print("-------------------------------------------------")
saker = ["dator", "telefon", "väska", 23]
#addera listorn

tredje = names + saker

print("---------ANDRA I LISTAN-----------------------")
print(tredje[len(names) + 1])

print("-------------------------------------------------")
# Bli två listor, tupples

fyra = names, saker

print(fyra[1][1])
for i in fyra:
    print(i)

print("-------------------------------------------------")
print("-------------------------------------------------")

print(names)
names.append("Adam")
names.remove("Sven")
names.sort()
del names[3]
print(names)
print("Lets pop and reverse")
print(names.pop(2))
names.reverse()
print(names)

print("-------------------------------------------------")
print("-------------------------------------------------")

names = ["Ny", "Lista", "Till", "Mig"]
colors = ["Bil", "Röd", "Blå", "Grön", "Lila"]
print(names)
print(colors)
print("---- swap ----")
names , colors = colors, names
print(names)

print("------------------- Sub-----------------------------")

names = ["Olof","Patrik","Sven", "Carl", "Adam", "Jeff", "Martin"]
print(names[2:-1])

print("-------------------TA BORT 2.0----------------------------")
for i in list(names):
    print(names)
    names.remove(i)
print(names)

print("--------------- SÖK -----------------------------")
names = ["Olof","Patrik","Sven", "Carl", "Adam", "Jeff", "Martin", "Carl"]

key = str.lower(input())

for i in names:
    if key == str.lower(i):
        print("hittade " + i)
        print("I index: {}".format(names.index(i)))

if key in names:
    print("The if statement found your key: ".format(key))
else:
    print("The if statement found nothing")

found = True if key in names else False
print(found)

found = names.index(key)
print("I found it at index: {}".format(found))

search = "finns ej"
for word in names:
    if word == key:
        search = "finn i listan"
        break
print(search)

print("--------------- TUPLES --------------------------")
print("-------------------------------------------------")

myTuple = (1 ,2 ,3 , "hej", "bilar")
print(myTuple)

myTuple = list(myTuple)
print(myTuple)
