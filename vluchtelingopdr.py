def vraag2() :

    print("Waar wil je heen vluchten?")
    print("a = Duitsland")
    print("b = Frankrijk")
    print("c = Engeland")

    antwoord2 = input()
    if antwoord2.lower() == "a":
        print ()
        print(vraag3())
    elif antwoord2.lower() == "b":
        print()
        print(vraag4())
    elif antwoord2.lower() == "c":
        print()
        print(vraag5())
    else:
        print("Kies a, b of c")

def vraag1() :

    print("Hoe wil je vluchten?")
    print("a = Auto")
    print("b = Boot")
    print("c = Vliegtuig")

    antwoord1 = input()
    if antwoord1.lower() == "a":
        print()
        print(vraag2())
    elif antwoord1.lower() == "b":
        print()
        print(vraag1())
    elif antwoord1.lower() == "c":
        print()
        print(vraag2())
    else:
        print("Kies a, b of c")

print (vraag1())
