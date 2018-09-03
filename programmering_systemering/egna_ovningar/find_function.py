def find2(astring, achar):
    ix = 0
    found = False

    while ix < len(astring) and not found:
        if astring[ix] == achar:
            found = True
        else:
            ix = ix + 1

    if found:
            return ix
    else:
            return -1
print(find2("Compsci", "o"))
print(find2("Compsci", "C"))
print(find2("Compsci", "s"))
print(find2("Compsci", "m"))
