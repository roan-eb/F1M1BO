print("\nWelkom bij mijn text based applicatie!\nVeel plezier!")

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
    print("\nJe bent in Turkije aangekomen wat is het eerste dat je gaat doen? \n(Eten zoeken/Onderdak zoeken)")
    print("A = Eten zoeken")
    print("B = Onderdak")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\nJe hebt eten gevonden, maar nog steeds geen onderdak.")
        vraag16()
    elif v2_2 == "B":
        print("\nJe hebt onderdak gevonden. Heel goed!")
        vraag18() 
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
        print("\nJe bent naar Nederland gegaan en krijgt daar onderdak bij een asielzoekerscentrum.")
        vraag11()
    elif v2_2 == "B":
        print("\nDuitsland neemt geen vluchtelingen meer aan, ze sturen je terug..")
        dood() 
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
        print("\nEr is alleen een probleem met deze bende..")
        vraag8()
    elif v2_2 == "B":
        print("\nJe bent verder gegaan met stelen zonder de bende.")
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
    print("\nWat zou je willen doen?\n(Supermarkt/Bezorgen)")
    print("A = Supermarkt")
    print("B = Bezorgen")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\nJe bent bij een supermarkt gaan werken.")
        vraag20()
    elif v2_2 == "B":
        print("\nJe hebt de baan gekregen en kon gelijk beginnen, maar al op je eerste werk dag werd je aangereden. Je beland in het ziekenhuis.")
        dood() 
    else:
        print("\nKies A of B\n")

        print(vraag10())

def vraag11():
    print("\nWil je daar blijven of wil je je familie opzoeken?\n(Blijven/Familie opzoeken)")
    print("A = Blijven")
    print("B = Familie opzoeken")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\nJe bent gebleven en krijgt eten en onderdak, maar de regering heeft nieuwe plekken nodig voor nieuwe asielzoekers.")
        vraag12()
    elif v2_2 == "B":
        print("\nJe gaat bij je familie wonen en leeft een normaal leven verder.")
        einde() 
    else:
        print("\nKies A of B\n")

        print(vraag11())

def vraag12():
    print("\nWaar ga je nu heen?\n(/)")
    print("A = Groningen")
    print("B = Amsterdam")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("Je bent naar groningen gegaan om daar een nieuw leven op te starten.\n")
        vraag13()
    elif v2_2 == "B":
        print("Je bent naar Amsterdam verhuisd, maar de huur is daar zo hoog dat je het niet meer kan betalen en je huis weer moet verkopen. Je word dakloos ...\n")
        dood() 
    else:
        print("\nKies A of B\n")

        print(vraag12())

def vraag13():
    print("\nJe krijgt daar een goede baan aangeboden. Neem je deze baan?\n(Ja/Nee)")
    print("A = Ja")
    print("B = Nee")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("Je vind daar je partner waar je later mee trouwt je word gelukking met een goede toekomst.\n")
        einde()
    elif v2_2 == "B":
        print("Je neemt de baan niet aan, maar wat nu?\n")
        vraag14() 
    else:
        print("\nKies A of B\n")

        print(vraag13())

def vraag14():
    print("\nJe zit te twijfelen of je een eigen bedrijf moet opstarten of een lot koopt want misschien win je wel die jackpot.\n(Eigen bedrijf/Lot)")
    print("A = Eigen bedrijf")
    print("B = Lot")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\nJe bent je eigen bedrijf begonnen. In het begin gaat het goed, maar dan komen er wat tegenslagen.")
        vraag15()
    elif v2_2 == "B":
        print("\nJe koopt een lot en wint de jackpot van 32,4 miljoen euro. Je verhuisd naar Dubai en geniet van je rijkdom!")
        einde() 
    else:
        print("\nKies A of B\n")

        print(vraag14())

def vraag15():
    print("\nHet bedrijf is bijna failliet je moet geld lenen of het verkopen.\n(Geld lenen/Verkopen)")
    print("A = Geld lenen")
    print("B = Verkopen")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\nJe leent geld van de bank en kan je bedrijf overeind houden, maar het was niet genoeg het bedrijf ging alsnog failliet je blijft zitten met een enorme restschuld.")
        dood()
    elif v2_2 == "B":
        print("\nJe verkoopt het bedrijf, maar je houd alsnog een grote schuld over en besluit om toch maar een normale baan te nemen bij een werkgever.")
        dood() 
    else:
        print("\nKies A of B\n")

        print(vraag15())

def vraag16():
    print("\nWaar wil je onderdak zoeken? Bij een asielzoekerscentrum of bij iemand?\n(Asielzoekerscentrum/Bij iemand)")
    print("A = Asielzoekerscentrum")
    print("B = Bij iemand")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\n")
        vraag17()
    elif v2_2 == "B":
        print("\nJe hebt bij iemand aangeklopt.")
        vraag19() 
    else:
        print("\nKies A of B\n")

        print(vraag16())

def vraag17():
    print("\n   \n(/)")
    print("A = ")
    print("B = ")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\n")
        vraag17()
    elif v2_2 == "B":
        print("\n")
        vraag4() 
    else:
        print("\nKies A of B\n")

        print(vraag17())

def vraag18():
    print("\nMaar je begint honger te krijgen \n(/)")
    print("A = ")
    print("B = ")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\n")
        vraag17()
    elif v2_2 == "B":
        print("\n")
        vraag4() 
    else:
        print("\nKies A of B\n")

        print(vraag18())

def vraag19():
    print("\nDe mensen vinden het prima als je bij hun verblijft. Ze bieden aan om op hun land te werken voor onderdak en eten. Wil je dit doen?\n(Ja/Nee)")
    print("A = Ja")
    print("B = Nee")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\nJe hebt besloten het te doen. Hierdoor bouw je een goede band op met de bewoners en kan je je leven weer opnieuw oppakken.")
        einde()
    elif v2_2 == "B":
        print("\nJe vind het aanzoek erg aardig maar je besluit toch om door te trekken.")
        vraag21() 
    else:
        print("\nKies A of B\n")

        print(vraag19())

def vraag20():
    print("\nTwee maanden later vragen ze of je leidinggevende wil worden want je doet het werk zo goed, maar je vind het eigenlijk niet heel leuk meer. Wat doe je?\nToch leidinggevende worden of een andere baan zoeken.\n(Leidinggevende/Andere baan)")
    print("A = Leidinggevende")
    print("B = Andere baan")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\nJe hebt de functie als leidinggevende genomen, waardoor je nu ook meer betaald kreeg en meer afwisselend werk hebt. Je krijgt weer meer zin in je baan.")
        einde()
    elif v2_2 == "B":
        print("\nJe bent gestopt bij de supermarkt, maar je kon geen betere baan vinden waardoor je de huur niet meer kon betalen..")
        dood() 
    else:
        print("\nKies A of B\n")

        print(vraag20())

def vraag21():
    print("\nDe volgende ochtend bedank je de mensen en trek je verder... \n(/)")
    print("A = ")
    print("B = ")

    v2 = input ()
    v2_2=v2.upper()
    if v2_2 == "A":
        print("\n")
        einde()
    elif v2_2 == "B":
        print("\n")
        vraag21() 
    else:
        print("\nKies A of B\n")

        print(vraag21())

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