""" Sträng formateringm med %
%s - sträng
%d - digit(int)
%f - float för att formatera hur många decimaler sätt %.xf där x är antal decimaler
%c - ett tecken (char)"""

name = "Sebastian"
age = 31
print("%c är första bokstaven, %s är mitt namn, %d+%d är mitt namn"%('s',name,age+age,age))

multiline = '''Hej
Här kommer flera rader
med text'''

mittfloat = 0.14000
print("%f"%(1/3))

# Antal decimaler
mittfloat = 0.14000
print("%.5f"%(0.14))


def calc_pay(h,r):
    if h > 40:
        return h*r+((h-40)*r*0.5)
    else:
        return h*r

#sum = calc_pay(int(input("Enter Hours: ")),int(input("Enter Rate: ")))
#print(type(sum))
#print("Your pay: %.f"%(sum))

#x = "computer"
#print(sorted("%s %s"%("Computer ","World ")))
#print(sorted(input("Hej :")))
#print()
#print(x.startswith("c"))

#print(str.startswith(input("Sträng? "), input("Börjar på? ")))
#print("{} {}".format(str.startswith(input("Sträng? "), input("Börjar på? ")), input("Skriv ut: ")))

my_string = "Nackademin är en skola jag går på och ligger på tomtebodavägen"
#print(input("Sträng: ") in input("Kolla din sträng mot:  "))

print(my_string.replace("är", "is"))
print(my_string)

print(str.split(input("Splitta: "), input("Seperator: "), int(input("how many: "))))
