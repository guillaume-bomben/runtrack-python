def rectangle(width, height):
    i=0
    longeur_trait = "-"*(width-2)
    longeur_vide = " "*(width-2)
    while i < height:
        if i == 0 or i == height-1 :
            print(f"|{longeur_trait}|")
        else:
            print(f"|{longeur_vide}|")
        i += 1

rectangle(10,3)