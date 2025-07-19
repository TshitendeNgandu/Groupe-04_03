activité= input("décrivez votre activité du jour :")
with open("journal.txt","a",encoding="utf-8") as f:
    f.write(activité + "\n")

print("activité ajouter dans 'journal.txt'.")
