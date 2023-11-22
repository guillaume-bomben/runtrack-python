def time_to_text(temp):
    heure = temp // 60
    minute = temp % 60
    print(f"{heure} heure et {minute} minutes")
    
time_to_text(65)
time_to_text(153)