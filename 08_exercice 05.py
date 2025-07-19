texte=input("entrer un texte :")
voyelle="aAEIOUYeiouy"
for ch in texte:
    if ch.isalpha() and ch not in voyelle:
        print(ch, end="")
        