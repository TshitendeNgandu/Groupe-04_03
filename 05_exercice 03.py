texte=input("entrer ine chaine :")
iverse=""
for m in texte.split():
    iverse= m + " " + iverse
print(f"la chaine inversée est : {iverse}")
