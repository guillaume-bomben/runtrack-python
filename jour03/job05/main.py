def calcule(num1 , operator , num2):
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    elif operator == "%":
        result = num1 % num2
    print(f"La resultat de {num1} {operator} {num2} est {result}")


calcule(10,"+",2)
calcule(10,"-",2)
calcule(10,"*",2)
calcule(10,"/",3)
calcule(10,"%",3)