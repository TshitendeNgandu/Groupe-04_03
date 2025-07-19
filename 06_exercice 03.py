somme=0
nb_note=0
while True:
    note=float(input("entrer note (entrer -1 pour arreter) :"))
    if note ==-1:
        break
    somme+=note
    nb_note+=1
if nb_note>0:
    moyenne= somme/nb_note
    print(f"la moyenne des notes est : {moyenne}")
else:
    print("Aucune note entrée")
