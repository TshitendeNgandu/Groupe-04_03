ht=int(input("Entrer le prix HT"))
taux_tva=int(input("entrer le taux TVA en %"))
taux_coéff=taux_tva/100
TTC= ht(1+taux_coéff)
print(f"montant TTC est : {TTC}")