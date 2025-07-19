role=input("Rôle (employé/visiteur/sécurité) :").lower()
if role == "rmployé":
    badge=input("Badge valide? (oui/non) :").lower()
    if badge=="oui":
        print("accès autorisé")
    else:
        print("accès refusé : badge invalide")
elif role=="visiteur":
    rdv=input("avez vous rendez-vous ? (oui/non) :")
    if rdv=="oui":
        print("accès autorisé")
    else:
        print("Accès refusé : pas de renez-vous")
elif role=="sécurité":
    print("accès autorisé")

else:
    print("accès refusé : rôle refusé")