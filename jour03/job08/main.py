def fruit_saison(type,saison):
    if type == "fruit" and saison == "hiver":
        print("orange, mandarine et kiwi")
    elif type == "fruit" and saison == "ete":
        print("Poire, fraise et cassis")
    elif type == "legume" and saison == "hiver":
        print("carrote, topinambour et endive")
    elif type == "legume" and saison == "ete":
        print("artichaut, aubergine et navet")
    else:
        print("Type ou/et Saison non valide")
        
fruit_saison("fruit","hiver")
fruit_saison("legume","hiver")
fruit_saison("fruit","ete")
fruit_saison("legume","ete")

fruit_saison("truc","ete")
fruit_saison("legume","truc")