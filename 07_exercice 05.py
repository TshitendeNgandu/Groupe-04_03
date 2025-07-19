ch=input("entrer des éléments :")
liste=ch.split()

inverse=[]
for i in range(len(liste)-1,-1,-1):
    inverse.append(liste[i])
print(f"liste inversée : {inverse}")

