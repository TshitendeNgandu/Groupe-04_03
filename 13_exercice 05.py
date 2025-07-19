import math
try:
    x=float(input("entrer un nombre :"))
    if x<0:
        raise ValueError("X négatif : racine non réelles")
    racine=math.sqrt(x)
except ValueError as e:
    print(f"Erreur : {e}")
else:
    print(f"racine carrée : {racine}")
finally:
    print("Fin du calcul.")
