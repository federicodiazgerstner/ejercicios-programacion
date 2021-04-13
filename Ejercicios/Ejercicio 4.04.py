def pasararomano(n):
    romanos = ["I", "V", "X", "L", "C", "D", "M"]
    decimales = [1, 5, 10, 50, 100, 500, 1000]
    digitos = []
    romano = ""
    
    while n > 0:
        digitos.append(n%10)
        n //= 10
        
    digitos.reverse()
    exp = len(digitos)
    
    for i in range(len(digitos)): #establece la potencia correspondiente.
        digitos[i] = digitos[i] * 10**(exp-1)
        exp -= 1
    
    for i in range(len(digitos)):
        if digitos[i] >= 1000:
            romano += "M" * (digitos[i] // 1000)
        elif 500 <= digitos[i] < 1000:
            if digitos[i] == 900:
                romano += "CM"
            else:
                romano += "D" + "C" * (digitos[i] // 100)
        elif 100 <= digitos[i] < 500:
            if digitos[i] == 400:
                romano += "CD"
            else:
                romano += "C" * (digitos[i] // 100)
        elif 50 <= digitos[i] < 100:
            if digitos[i] == 90:
                romano += "XC"
            else:
                romano += "L" + "X" * (digitos[i] // 10)
        elif 10 <= digitos[i] < 50:
            if digitos[i] == 40:
                romano += "XL"
            else:
                romano += "X" * (digitos[i] // 10)
        elif 5 <= digitos[i] <= 10:
            if digitos[i] == 9:
                romano += "IX"
            else:
                romano += "V" + "I" * (digitos[i] - 5)
        elif 1 <= digitos[i] < 5:
            if digitos[i] == 4:
                romano += "IV"
            else:
                romano += "I" * digitos[i]
    
    return romano



#programa principal
n = int(input("Ingrese un número decimal a ser convertido a romano: "))
r = pasararomano(n)
print(f"El número {n} es igual a {r} en romano.")