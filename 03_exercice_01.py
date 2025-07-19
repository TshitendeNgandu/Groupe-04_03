n=int(input("Entrer votre âge :"))
p=input("entrer votre pays d'origine ").lower()
if n>=18 and p=="congo" or "cameroun":
    print("Inscription autorisée")
elif n<18:
    print("Désolé, mais vous êtes trop jeune pour ce programme")
else:
    print("malheureusement, le programme  est pour les ressortissants du Congo ou cameroun")