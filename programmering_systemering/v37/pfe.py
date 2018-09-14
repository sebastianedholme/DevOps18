try:
    hours = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))
except:
    print("Enter only numbers..")

if hours >= 40:
    print("Pay: " + str(1.5 * hours * rate - 20 * rate))
else:
    print("Pay: " + str(rate * hours))
