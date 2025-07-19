mots=input("saisissez une liste de mots avec des espaces").split()
voyelle="aeiouy"
total=0
for mot in mots:
    for lettre in mot:
        if lettre in voyelle:
            total+=1
print(f"nombre total de voyelle : {total}")

