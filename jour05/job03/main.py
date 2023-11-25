def triangle(height):
    left_vide = " " * (height -1) ; center_vide = "" ; i=0
    while i < height:
        if i != height -1:
            print(f"{left_vide}/{center_vide}\\")
            left_vide = " " * (height - (i+2)) ; center_vide += "  "
        else :
            center_ligne = "_" * len(center_vide)
            print(f"{left_vide}/{center_ligne}\\")
        i += 1


triangle(5)