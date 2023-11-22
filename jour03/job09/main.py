def moyenne(note1, note2, note3):
    moyenne_etudiant = (note1 + note2 + note3)/3
    if  15 <= moyenne_etudiant <=20:
        print(f"Moyenne : {moyenne_etudiant} \n Tres bon élève")
    elif  11 <= moyenne_etudiant <=14:
        print(f"Moyenne : {moyenne_etudiant} \n Bon élève")
    elif  8 <= moyenne_etudiant <=10:
        print(f"Moyenne : {moyenne_etudiant} \n Elève moyen")
    if  0 <= moyenne_etudiant <= 7:
        print(f"Moyenne : {moyenne_etudiant} \n Elève devant faire des efforts")
        
moyenne(18,18,18)
moyenne(13,13,13)
moyenne(9,9,9)
moyenne(5,5,5)
