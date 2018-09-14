x = [i for i in range(10)]
x[2] = "f"
print(x[0:4])
print()

for row in range(5):
    print("-")
    for col in range(4):
        print("a", end="")
    print()
