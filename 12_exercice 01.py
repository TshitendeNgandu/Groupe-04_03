utilisateur=[]
while True:
    nom=input("entrer nom d'utilisateur (ou stop pour arrêter) :").lower()
    if nom=="stop":
        break
    utilisateur.append(nom)
with open("utilisateur.txt","w", encoding="utf-8") as f:
    for u  in utilisateur:
        f.write(u+"\n")

print("utilisateurs enregistrés dans 'utilisateurs.txt'.")


