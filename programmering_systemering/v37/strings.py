"""
Here is a multiline commentary. This file contains some
python3 repetitions working with strings.
"""


print("Hello this is a string 'ok ok'")
print("Hello this is a string \"ok ok\" some clarity")
print("Hello \nThis ia new line \nand another")
print("Hello \nThis ia newline \nand another" + " " + "Hello string \"ok ok\" some clarity")

line = "This is a string \n With some new lines on"

x = 1001010101010101111111111111111
x = 0.2

print(type(x))

x = "10"
print(x)
print(type(x))
print(type(int(x)))

mylist = [123, "hello", 0.2, x, "J"]

print(mylist)
print("---------------------clear list------------------------------")
mylist.clear()
print(mylist)
print("cleared\n")

x = [i for i in range(9)]
print(x)

x = [i**2 for i in range(9)]
print(x)

print("\n---- MEGA LISTS ----")
list1 = [1 ,2, 3]
list2 = [4 ,5, 6]
list3 = [7, 8, 9]

mega_list = [list1, list2, list3]
print(mega_list)
mega_list = [i for i in list1+list2+list3]
print(mega_list)

print("\nEasier ---------------------------------------------------\n")
# How to do a simpler append 
mega_list2 = list1 + list2 + list3
print(mega_list2)

print("Create multiple lists in list")
mega_list3 = [[i for i in range(10)],[i for i in range(20)]]
print(mega_list3)
