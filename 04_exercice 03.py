f=input("avez-vous de la fièvre ? (oui/non) ")
if f =="oui":
    d=input("avez-vous des douleurs ? (oui/non)")
    if d=="oui":
        print("consultez un medecin")
    else:
        print("surveillez votre santé.")
else:
    t=input("avez-vous de la toux ? (oui/non)")
    if t=="oui":
        print("Repos conseiller")
    else:
        print("Bonne santé !")