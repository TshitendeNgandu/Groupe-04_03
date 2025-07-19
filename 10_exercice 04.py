num=input("entrer un numéro de téléphone (10 chiffres) :")
if len(num)>3:
    masque="*"*(len(num)-3)+num[-3:]

print(f"numéro masqué est ,{masque}")


