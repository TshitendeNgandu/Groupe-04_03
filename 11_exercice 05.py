import random
import string
def genrateur_mdp(longeur):
    caracteres=string.ascii_letters+string.digits
    mdp=" ".join(random.choice(caracteres) for _ in range(longeur))
    return mdp
longueur=int(input("longueur de mot de passe :"))
a=genrateur_mdp(longueur)
print(f"mot de passe : {a}")
