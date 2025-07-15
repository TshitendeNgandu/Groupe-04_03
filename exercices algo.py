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

#-----------------------

#deuxième programme
produit="Smartphone"
prix=300.0
stock=50
remise=0.20
#calcul du orix final
prix_final=prix*(1-remise) 
#affichage 
print(f"Produit : {produit}")
print(f"Prix : {prix}$")
print(f"remise : {remise * 100}%")
print(f"Prix final après remise : {prix_final}$")
print(f"Stock de produit : {stock}")

#---------------------------------------

#programme 3
heures=int(input("heures :"))
minutes=int(input("minutes :"))
secondes=int(input("secondes :"))

#durée en secondes 
durée= heures*3600 + minutes*60 + secondes
print(f" la durée en secondes est : {durée} secondes.")

#------------------------------------------

#programme 4
notes= float(input("Entrer la note :"))
notes=(notes/20)*100
print(f"Sur 100, la note est : {notes}")

#-------------------------------------------

#programme 4
distance_Km=float(input("Entrer la distance en kilometre"))
temps_heure=float(input("Entrer le temps en heures"))
vitesse1= distance_Km / temps_heure
vitesse2= (distance_Km*1000) / (temps_heure*3600)
print(f"Vitesse en km/h est : {vitesse1}")
print(f"Vitesse en m/s est : {vitesse2}")

#-----------------------------------
# 2. Opérateurs de base et saisie
# programme 1
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
#--------------------------------
# programme 2
n=int(input("entrer un nombre entier :"))
if n%5==0 and n%3==0:
    print(n," est divisible par 3 et 5")
else :
    print(n,"n'est pas divisble par 3 et 5 en même temps")
#---------------------------------
#programme 3
ht=int(input("Entrer le prix HT"))
taux_tva=int(input("entrer le taux TVA en %"))
taux_coéff=taux_tva/100
TTC= ht(1+taux_coéff)
print(f"montant TTC est : {TTC}")

#-------------------------------------


#programme 4

a=float(input("entrer la première note :"))
b=float(input("entrer la première note :"))
c=float(input("entrer la première note :"))
moyenne=(a+b+c)/3
if moyenne >=10:
    print("l'étudiant est reçu.")
else:
    print("L'étudiant n'est pas reçu")

#---------------------------------
#programme 5
n=float(input("entrer montant en USD :"))
eur=n*0.93
cfa=n*610
gbp=n*0.79
print(f"montant en euro : {eur}")
print(f"montant en cfa : {cfa}")
print(f"montant en gbp : {gbp}")

#-----------------------------
#3. Condition
n=int(input("Entrer votre âge :"))
p=input("entrer votre pays d'origine ").lower()
if n>=18 and p=="congo" or "cameroun":
    print("Inscription autorisée")
elif n<18:
    print("Désolé, mais vous êtes trop jeune pour ce programme")
else:
    print("malheureusement, le programme  est pour les ressortissants du Congo ou cameroun")

#----------------------------
#programme 2
a=float(input("Enter la note :"))
if n>=90:
    print("Excellent !")
elif n>=75:
    print("Très bien")
elif n>=60:
    print("Bien")
elif n>=50:
    print("Passable")
else :
    print("insuffisant")

#---------------------------------------
#programme 2
n=float(input("montant du panier :"))
if n >=100:
    frais=0
elif n>=50:
    frais=5
else:
    frais=10
total=n+frais

print(f"frais de livraison = {frais}")
print(f"montant total est = {total}")

#-------------------------------
# programme 4
temp=float(input("Entrer la température :"))
if temp>=35:
    print("très chaud : rester hydraté")
elif temp >=25:
    print("chaud, faites attention au soleil")
elif temp>=15:
    print("température agréable")
else :
    print("il fait frais, couvrez-vous.")
#--------------------------------------
# programme 5
mdp=input("Entrer un mot de passe")
if len(mdp)>=8 and any(c.isdigit() for c in mdp) and any(c.isupper() for c in mdp):
    print("mot de passe valide")
else:
    print("mot de passe invalide")

#------------------------------
# Conditions enchainées et instructions imbriquées
#programme 1
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

        

