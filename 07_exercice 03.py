n=input("entrer des nombres :")
liste=[float(c) for c in n.split()]
max=max(liste)
min=min(liste)
moyenne=sum(liste)/len(liste)

print(max)
print(min)
print(f"{moyenne:.2f}")

