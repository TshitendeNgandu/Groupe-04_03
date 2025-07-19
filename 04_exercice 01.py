a=int(input("age :"))
statut=input("statut : (étudiant/salarié/retraité) :").lower()
if a<18:
    tarif=5
else :
    if 18<=a<=25:
        if statut=="étudiant":
            tarif=6
        elif statut=="salarié":
            tarif=8
        else:
            tarif=10
    else:
        if statut=="retraité":
            tarif=7
        else :
            tarif=10

print(f"votre tarif est {tarif}$.")   