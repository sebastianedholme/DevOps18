person = { "Namn": input("Vad är ditt förnamn? "), "Efternamn": input("Vad är ditt efternamn? "), "Skola": input("Vilken skola går du på? ") }

print("Hej {} {}, vad roligt att du går på {}".format(person["Namn"], person["Efternamn"], person["Skola"]))
