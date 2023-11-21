a = int(input("entrez une longeur a : ")) 
b = int(input("entrez une longeur b : ")) 
c = int(input("entrez une longeur c : ")) 

longeur = sorted([a,b,c])
part = 0

if longeur[2] < longeur[0] + longeur[1]:
    print("Ce triange est posible")
    if longeur[2]**2 == longeur[0]**2+ longeur[1]**2:
        print("Le Triange est rectangle")
        part += 1
    if longeur[0] == longeur[1] == longeur[2]:
        print("Le Triangle est equilateral")
        part += 1
    elif longeur[0] == longeur[1] or longeur[1] == longeur[2] or longeur[2] == longeur[0]:
        print("Le Triangle est isocele")
        part += 1
    if part == 0 :
        print("Le Triangle est quelconque")

else :
    print("Ce triangle n'est pas possible")