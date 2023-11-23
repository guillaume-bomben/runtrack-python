def incre(L):
    print(L)
    i=0
    while i <len(L):
        L[i] += 1
        i += 1
    print(L)
    
L = [7, 11, 42, 39, 2]
incre(L)