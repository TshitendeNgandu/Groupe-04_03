def est_palindrome(mot):
    if mot == mot[::-1]:
        print(f"{mot} est un palindrome")
    else:
        print(f"{mot} n'est pas un palindrome")

mot=input("Entrer un mot :")
est_palindrome(mot)
