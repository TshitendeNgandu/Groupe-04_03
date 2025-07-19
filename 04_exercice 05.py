p=input("choisissez un plat (viande, poisson, végétarien) :").lower()
if p=="viande":
    c=input("cuisson (saignant/ à point/ bien cuit) :").lower()
    print(f"vous avez choisit {c}")
elif p=="poisson":
    s=input("sauce (citron/beurre) :")
    print(f"vous avez choisi {s}")
elif p=="végétarien":
    a=input("souhaitez-vous des salades ou des pates ? ").lower()
    print(f"Vous avez choisi {a}")
else:
    print("choix invalide")