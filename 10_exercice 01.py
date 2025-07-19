mot=input("entrer un mot (min 5 letrres) :")
if len(mot)>=5:
    milieu=mot[2:-2]
    print(f"Partie centrale : {milieu}")
else:
    print("mot trop court")

