def convert(usd):
    eur= 0.93*usd
    cfa= 610*usd
    gdp=0.79*usd
    return eur,cfa, gdp
usd=float(input("entrer un montant en usd "))
a,b,c=convert(usd)
print(f"{usd} usd vaut {a} euro, {b} cfa, {c} gdp")
