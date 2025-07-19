nbre=int(input("nombre pour la table de multiplication :"))
with open("table.txt","w",encoding="utf-8") as f:
    for i in range(1,13):
        ligne= f"{nbre} * {i} = {nbre*i}\n"
        f.write(ligne)
print("table générée dans 'table.txt'.")

