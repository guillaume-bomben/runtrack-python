def pair_impair(nombre):
    if nombre < 0 or type(nombre)!=int:
        print("Le nombre n'est pas positif ou un entier")
    else:
        if nombre%2 == 0:
            print(f"Le nombre {nombre} est pair")
        else:
            print(f"Le nombre {nombre} est impair")

pair_impair(10)
pair_impair(9)
pair_impair(9.8)