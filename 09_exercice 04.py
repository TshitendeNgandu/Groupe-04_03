phr=input("entrer une phrase ou un titre :")
mots=phr.split()
acronyme=""
for mot in mots :
    acronyme += mot[0].upper()
print(f"l'acronyme de ce titre est {acronyme}")

