n=input("entrer des nombres séparées par des espaces")
liste=[int(x) for x in n.split()]
somme_pair=0
for i in liste:
    if i%2==0:
        somme_pair+=i
print(f"somme des nombres pairs est : {somme_pair}")
