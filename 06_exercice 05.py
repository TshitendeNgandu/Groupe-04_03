n=int(input("entrer un nombre entier positif:"))
while n<0:
    print("veuillez entrer un nombre positif :")
    n=int(input("entrer un nombre entier positif:"))
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
    
print(f"factorielle de {n} = {fact}")
