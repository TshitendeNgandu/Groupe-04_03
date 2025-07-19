texte=input("entrer une phrase :").lower()
mot=input("mot que vous cherchez :").lower()
compte=texte.count(mot)
print(f"le mot '{mot}'apparait {compte} fois dans la phrase")
