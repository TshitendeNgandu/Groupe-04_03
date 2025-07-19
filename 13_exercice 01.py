try:
    a=float(input("entrer nombre 1 :"))
    b=float(input("entrer nombre 2 :"))
    result=a/b
except ZeroDivisionError:
    print("division par 0 impossible.")
else:
    print(f"resultat : {result}")
    