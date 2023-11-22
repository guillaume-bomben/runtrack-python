def pair_inpair(nombre):
    if nombre < 0 or type(nombre)!=int:
        print("Le nombre n'est pas positif ou un entier")
    else:
        if nombre%2 == 0:
            print(f"Le nombre {nombre} est pair")
        else:
            print(f"Le nombre {nombre} est impair")

pair_inpair(10)
pair_inpair(9)

pair_inpair(9.8)