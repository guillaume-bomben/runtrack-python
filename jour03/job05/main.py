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
    return f"La resultat de {num1} {operator} {num2} est {result}"


print(calcule(10,"+",2))
print(calcule(10,"-",2))
print(calcule(10,"*",2))
print(calcule(10,"/",3))
print(calcule(10,"%",3))