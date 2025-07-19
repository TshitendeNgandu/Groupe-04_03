entree=input("entrer des nombres entiers séparées par des espaces")
liste=[int(c)for c in entree.split()]
n=len(liste)
for i in range(n):
    for j in range(0, n-i-1):
        if liste[j]>liste[j+1]:
            liste[j],liste[j+1]=liste[j+1],liste[j]
print(f"liste triée : {liste}")
