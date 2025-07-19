a=int(input(" années d'ancienneté :"))
n=int(input("note de performance (1 à 5):"))
if a>=5:
    if n>=4:
        print("Prime : 2000 $")
    else:
        print("Prime : 1000$")
else:
    if n>=4:
        print("Prime : 500 $")
    else:
        print("Pas de prime")