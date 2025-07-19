def stats(liste):
    somme=sum(liste)
    moyenne=somme/len(liste)
    maximum=max(liste)
    return somme, moyenne, maximum
liste=[int(x) for x in input("entrer une liste de nombre separées par des espaces ").split()]
s,m,mx=stats(liste)
print(f"la somme = {s}, la moyenne = {m}, maximum = {mx}")



