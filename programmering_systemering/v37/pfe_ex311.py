def return_score(x):
    if x > 1.0:
        return "Bad score" 
    elif x >= 0.9:
        return "A" 
    elif x >= 0.8:
        return "B"
    elif x >= 0.7:
        return "C"
    elif x >= 0.6:
        return "D"
    else:
        return "F"

try:
    points = float(input("Enter a score to findout grade: "))
except:
    print("Bad input!")

print(return_score(points))
