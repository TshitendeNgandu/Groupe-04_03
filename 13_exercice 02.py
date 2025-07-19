valeur=input("entrer un entier :")
try:
    int(valeur)
except ValueError:
    print("Vous n'avez pas entré un entier correct")
else:
    print(f"entier entré est {valeur}")
