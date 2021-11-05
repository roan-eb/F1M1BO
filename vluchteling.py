print("\nWelkom bij mijn text based applicatie!\nMijn game is gebaseerd op het verhaal van Sara, zij moest uit Syrië vluchten en kwam uitendelijk in Nederland terecht.\nLaten we beginnen!")

def vraag1():
    print("\nEr onstaat oorlog in Syrië het land waar je geboren bent. Wat doe je? \n(Vluchten/Afwachten)")
    print("A = Vluchten")
    print("B = Afwachten")

    v1= input ()
    v1_1=v1.upper()
    if v1_1 == "A":
        print("\nHeel goed je bent net op tijd gevlucht!")
        vraag2()
    elif v1_1 == "B":
        print("\nAfwachten was niet zo'n goede keuze de oorlog werd erger..\n")
        dood() 
    else:
        print("\nKies A of B\n")

        vraag1()

def vraag2():
    print("\nJe hebt besloten te vluchten, maar naar welk land? \n(Turkije/Libanon)")
    print("A = Turkije")
    print("B = Libanon")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\nJe hebt besloten om naar Turkije te gaan!")
        vraag4()
    elif v2_2 == "B":
        print("\nJe bent naar Libanon gegaan heel goed!")
        vraag3() 
    else:
        print("\nKies A of B\n")

        print(vraag2())

def vraag3():
    print("\nWil je daar blijven of wil je naar Europa toe? \n(Blijven/Europa)")
    print("A = Blijven")
    print("B = Europa")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\nJe bent in Libanon gebleven, maar er is een probleem..")
        vraag5()
    elif v2_2 == "B":
        print("\nEuropa klinkt wel leuk.")
        vraag7() 
    else:
        print("\nKies A of B\n")

        print(vraag3())

def vraag4():
    print("\nJe bent in Turkije aangekomen wat is het eerste dat je gaat doen? \n(Eten/Onderdak)")
    print("A = Eten")
    print("B = Onderdak")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("ietss \n")
        vraag4()
    elif v2_2 == "B":
        print("ietss \n")
        vraag4() 
    else:
        print("\nKies A of B\n")

        print(vraag4())

def vraag5():
    print("\nJe hebt namelijk geen geld meer en geen bezittingen meegenomen. Wat doe je? \n(Stelen/Werk zoeken)")
    print("A = Stelen")
    print("B = Werk zoeken")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\nJe bent gaan stelen...")
        vraag6()
    elif v2_2 == "B":
        print("\nJe bent gaan zoeken naar werk.")
        vraag10() 
    else:
        print("\nKies A of B\n")

        print(vraag5())

def vraag7():
    print("Naar welk land in europa wil je gaan? (Nederland/Duitsland)")
    print("A = Nederland")
    print("B = Duitsland")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("iets\n")
        vraag7()
    elif v2_2 == "B":
        print("iets\n")
        vraag7() 
    else:
        print("Kies A of B")

        print(vraag7())

def vraag6():
    print("\nJe komt daarbij in aanraking met een bende. Wil je de bende joinen? \n(Ja/Nee)")
    print("A = Ja")
    print("B = Nee")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("Er is alleen een probleem met deze bende..\n")
        vraag8()
    elif v2_2 == "B":
        print("Je bent verder gegaan met stelen zonder de bende.\n")
        vraag9() 
    else:
        print("\nKies A of B\n")

        print(vraag6())

def vraag8():
    print("\nDe gang blijkt erg gevaarlijk te zijn en de politie is ze al op het spoor. Wat doe je? \nWegrennen/Blijven")
    print("A = Wegrennen")
    print("B = Blijven")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("Je hebt besloten om weg te rennen, maar nu ben je nog geen stap verder helaas..\n")
        vraag6()
    elif v2_2 == "B":
        print("Je hebt besloten bij de gang te blijven, maar twee dagen later doet de politie een inval en pakt de hele bende op... Je beland in de gevangenis en krijgt levenslang de bende had namelijk meerdere moorden gepleegd.\n")
        dood() 
    else:
        print("\nKies A of B\n")

        print(vraag8())

def vraag9():
    print("\nHet gaat zo goed dat je nu huur kan betalen. Wil je verder blijven gaan met stelen of een echte baan gaan zoeken? \n(Blijven stelen/Echte baan zoeken)")
    print("A = Blijven stelen")
    print("B = Echte baan zoeken")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\nHet bent zo goed in het stelen dat je een eigen bende opzet die erg succevol word. Je word steen rijk en kan alles kopen wat je maar wil. Goed gedaan!")
        einde()
    elif v2_2 == "B":
        print("\nJe hebt er voor gekozen om nu een normale baan te nemen, maar je krijgt opeens veel minder betaald en kan daardoor je huur niet meer betalen.. Je beland weer op straat.")
        dood() 
    else:
        print("\nKies A of B\n")

        print(vraag9())

def vraag10():
    print("\nWat zou je willen doen? \n(Supermarkt/Bezorgen)")
    print("A = Supermarkt")
    print("B = Bezorgen")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\n....")
        vraag6()
    elif v2_2 == "B":
        print("\n....")
        vraag6() 
    else:
        print("\nKies A of B\n")

        print(vraag10())



def dood():
    restart=input("Opniew spelen? ja/nee\n")
    restart_1=restart.upper()
    if restart_1=='JA':
        vraag1()
    elif restart_1=='NEE':
        ()
    else:
        print("type ja of nee")
        dood()
vraag1()

def einde():
    restart=input("Je hebt het spel uitgespeeld goed gedaan! Wil je opniew spelen? (ja/nee)\n")
    restart_1=restart.upper()
    if restart_1=='JA':
        vraag1()
    elif restart_1=='NEE':
        ()
    else:
        print("type ja of nee")
        einde()
vraag1()