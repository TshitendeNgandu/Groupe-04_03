fichier=input("entrer nom du fichier à lire :")
try:
    with open(fichier,"r", encoding="utf-8") as f:
        contenu=f.read()
except FileNotFoundError:
    print("Erreur : fichier introuvable")
else:
    print("contenu du fichier")
    print(contenu)
    