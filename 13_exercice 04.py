while True:
    try:
        n=input("entrer un réel postif")
        if n<0:
            raise ValueError ("Nbre négatif interdit !")
        break
    except ValueError as e:
        print(f"Erreur : {e}")

print(f"vous avez saisi {n}")
