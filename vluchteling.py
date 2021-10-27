answer_yes = ["Ja", "J", "ja", "j", "Europe", "europa"]
answer_no = ["Nee", "N", "nee", "n", "Buurland", "buurland"]

print("""

Er onstaat oorlog in Syrie het land waar je geboren bent. Wat doe je?
Ga je vluchten of niet? (Ja / Nee)
""")

ans1 = input(">>")

if ans1 in answer_yes:
    print("\nJe hebt besloten te vluchten, maar waar ga je heen? Naar een van de buurlanden of Europa? (Europa / Buurland)\n")

    ans2 = input(">>")

    if ans2 in answer_yes:
        print("\nJe hebt besloten naar Europa te gaan")

    elif ans2 in answer_no:
        print("\nJe hebt besloten om naar het buurland Libanon te gaan, daar is het nog veilig zonder oorlog.")

    else:
        print("\nDat is geen geldig antwoord! ")

elif ans1 in answer_no:
    print("\nDe oorlog word erger  (  / )\n")

    ans3 = input(">>")

    if ans3 in answer_yes:
        print("\n")

    elif ans3 in answer_no:
        print("\n")

    else:
        print("\nDat is geen geldig antwoord! ")

else:
    print("\nDat is geen geldig antwoord! ")