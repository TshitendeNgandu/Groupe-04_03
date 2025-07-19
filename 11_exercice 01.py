def calculer(a,b,op):
    if op=="+":
        return a+b
    if op=="-":
        return a-b
    if op=="*":
        return a*b
    if op=="/":
        if not b==0:
            return a/b
        else:
            return "division par 0 impossible."
    else:
        print("introduire des nombres et des opérations simples ")
a=float(input("entrer un premier nombre :"))
b=float(input("entrer un deuxième nombre :"))
op=input("entrer une opération (+/-/*//) :")
resultat=calculer(a,b,op)
print(f"resultat = {resultat}")
