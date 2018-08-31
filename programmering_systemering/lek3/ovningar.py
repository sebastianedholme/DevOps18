# coding=utf-8

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
