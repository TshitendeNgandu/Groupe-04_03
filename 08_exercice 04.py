count=0
mots=[]
ph=input("entrer une phrase :").split()
for mot in ph:
    if len(mot)>5:
        count+=1
        mots.append(mot)
print(f" il y a {count} mots qui ont plus de 5 lettres qui sont {mots} ")


