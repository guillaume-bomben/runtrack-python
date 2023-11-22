def signe(nombre):
    if nombre < 0 :
        print(f"Le nombre {nombre} est negatif")
    elif nombre > 0 :
        print(f"Le nombre {nombre} est positif")
    else:
        print("Le nombre est egale a zero")

signe(10)
signe(-10)
signe(0)