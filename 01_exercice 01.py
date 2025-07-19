# demande informations à l'utilisateur
prenom=input("Entrez votre prénom :")
age=int(input("Entrez votre âge :"))
ville=input("Entrez votre ville :")
metier=input("Entrez votre metier :")

#approximation des jours vécus
jours_vécus=age*365

#affichage formaté

print("\n === Profil utilsateur ===")
print(f"Prénom : {prenom}")
print(f"Age : {age}")
print(f"Ville : {ville}")
print(f"Metier : {metier}")
