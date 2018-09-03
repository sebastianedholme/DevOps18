# print("--------------------------------------------------------")
# while True:
#     number = int(input("Välj en siffra att höja upp n^1-10: "))
#     for n in range(1, 11):
#         print("{}^{} is = {}".format(number, n, number**n))
#     if str.lower(input("Vill du fortsätta, Ja/Nej? ")) == "nej":
#         print("Hej då!")
#         break
# print("--------------------------------------------------------")
# while True:
#     print("""välj en operand att räkna med
#     1. addition
#     2. multiplikation
#     3. exponentiell
#     4. avsuta""")
#     val = int(input("val: "))

#     if val != 4:
#         number = int(input("Välj en siffra att räkna med: "))
#         n = int(input("Välj en andra siffra att räkna med: "))

#         if val == 1:
#             print(number+n)
#         elif val == 2:
#             print(number*n)
#         elif val == 3:
#             print(number**n)
#     else:
#         print("Hej då!")
#         break
# print("--------------------------------------------------------")
print("------------------------------DICTIONARY---------------------")

import operator
ops = { "+": operator.add, "*": operator.mul, "**": operator.pow}
while True:
    print("""Välj en operand och två siffror för att räkna:
     + | Addition
     * | Multiplkation
    ** | Exponetial
     a | Avsluta""")

    val = input("Ditt val: ")

    if str.lower(val) == "a":
        break

    num1 = int(input("Välj en siffra att räkna med: "))
    num2 = int(input("Välj en andra siffra att räkna med: "))
    print("\n Svaret på {} {} {} = {}\n".format(num1, val, num2, ops[val](num1,num2)))
    """
    ops blir värdet på nyckeln jag valt -> ops[val]
    Då kan jag ge funktionen jag stoppat in som värde två argument som funktionen tar (num1,num2)
    """

print("-------------------------------DICTIONARY-------------------------")

