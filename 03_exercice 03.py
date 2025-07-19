n=float(input("montant du panier :"))
if n >=100:
    frais=0
elif n>=50:
    frais=5
else:
    frais=10
total=n+frais

print(f"frais de livraison = {frais}")
print(f"montant total est = {total}")