a=float(input("entrer un premier nombre"))
b=float(input("entrer un seuxième nombre"))

somme=a+b
difference=a-b
produit= a*b
quotient_réelle= a/b if b !=0 else "division par 0 impossible"
quotient_entier= a//b if b!=0 else "division par 0 impossible"
reste= a%b if b!=0 else "division par 0 impossible"
#affichage des resultats
print(f"Somme : {somme}")
print(f"différence : {difference}")
print(f"produit : {produit}")
print(f"quotient : {quotient_réelle}")
print(f"division entière : {quotient_entier}")
print(f"reste : {reste}")