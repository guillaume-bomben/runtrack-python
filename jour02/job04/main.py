nombre = int(input("Entrez un entier superieur a zero : "))
i=1

while i <= nombre:
    print(f"table de multiplication de {i} : ")
    j=1
    while j <=10:
        print(f"{i} x {j} = {i*j}")
        j +=1
    j= 1
    i +=1
