n=input("entrer des valeurs (séparées par des espaces)")
liste=n.split()
unique=[]
for item in liste:
    if not item in unique:
        unique.append(item)
print(f"liste sans doublons : {unique}")

