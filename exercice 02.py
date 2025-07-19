produit="Smartphone"
prix=300.0
stock=50
remise=0.20
#calcul du orix final
prix_final=prix*(1-remise) 
#affichage 
print(f"Produit : {produit}")
print(f"Prix : {prix}$")
print(f"remise : {remise * 100}%")
print(f"Prix final après remise : {prix_final}$")
print(f"Stock de produit : {stock}")