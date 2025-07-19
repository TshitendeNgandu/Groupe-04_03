carré=[]
for i in range(1,21):
    carré.append(i**2)

print(f"les carrées sont : {carré}")
carrés=[]
for val in carré:
    if val >100:
        carrés.append(val)
print(f"les carrés sup à 100 sont : {carrés}")
