notes=[float(x) for x in input("entrer des notes :").split()]
moyenne=sum(notes)/len(notes)
with open("statistique.txt","w",encoding="utf-8") as f:
    f.write(f"notes = {notes} \n")
    f.write(f"moyenne = {moyenne:.2f} \n")
    
print("statistique sauvegardées dans 'statistique.txt'.")


