produit="apple"
prix=1
quantite=10

print("Prix initial et stock de Basse :")
print( produit  + " : " + str(prix)  + " €/unité , " +  str(quantite) + " unité(s)")

quantite += int(input("Nombre de produit a ajouter : \n"))
prix *= 1.1

print("Prix et stock augmenter :")
print( produit  + " : " + str(prix)  + " €/unité , " +  str(quantite) + " unités")