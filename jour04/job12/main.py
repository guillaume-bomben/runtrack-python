def mini(L):
    min = L[0]
    for i in L:
        if i < min:
            min = i
    return min

def trie(L):
    print(f"La liste avant trie : {L}")
    Lc = L
    l_trier = []
    while Lc:
        l_trier.append(mini(Lc))
        Lc.remove(mini(Lc))
    return l_trier

L = [7, 11, 42, 39, 2]
print(trie(L))