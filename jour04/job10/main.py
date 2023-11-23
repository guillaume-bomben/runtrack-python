def add_comp(L):
    somme = 1
    for i in L:
        if 90>=i>=25:
            somme *= i
    print(somme)

L=[8,24,27,48,2,16,9,7,84,91]
add_comp(L)