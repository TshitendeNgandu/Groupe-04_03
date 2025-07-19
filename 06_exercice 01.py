import random
nbre_secret=random.randint(1,100)
essai= None
while not essai==nbre_secret:
    essai=int(input("essaie un nombre"))
    if essai<nbre_secret:
        print("trop petit !")
    elif essai>nbre_secret:
        print("trop grand !")
    else:
        print("Bravo tu as trouvé !")
        