distance_Km=float(input("Entrer la distance en kilometre"))
temps_heure=float(input("Entrer le temps en heures"))
vitesse1= distance_Km / temps_heure
vitesse2= (distance_Km*1000) / (temps_heure*3600)
print(f"Vitesse en km/h est : {vitesse1}")
print(f"Vitesse en m/s est : {vitesse2}")