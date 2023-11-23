def nb_mul_3(L):
    nb = 0
    for i in L:
        if i%3 == 0 :
            nb +=1
    print(f"La liste contient {nb} multiple de 3")

L = [8,24,48,2,16]
nb_mul_3(L)