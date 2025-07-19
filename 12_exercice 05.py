texte=input("entrer une phrase :")
nb_mots=len(texte.split())
nb_caractere=len(texte)
with open("rapport.xtx","w", encoding="utf-8") as f:
    f.write("===Rapport d'Analyse=== \n")
    f.write(f"Phrase : {texte}\n")
    f.write(f"Nombre de mots : {nb_mots}\n")
    f.write(f"Nombre de caractères : {nb_caractere}\n")

print("Rapport dauvegardé dans 'rapport.txt'.")

