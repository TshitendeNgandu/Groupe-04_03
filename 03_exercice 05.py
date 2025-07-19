mdp=input("Entrer un mot de passe")
if len(mdp)>=8 and any(c.isdigit() for c in mdp) and any(c.isupper() for c in mdp):
    print("mot de passe valide")
else:
    print("mot de passe invalide")