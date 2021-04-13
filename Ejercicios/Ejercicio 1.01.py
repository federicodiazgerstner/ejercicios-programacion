def retornaMayorEstricto(a, b, c):
    """Toma tres valores y retorna el mayor estricto, o -1 de no existir / no ser estricto."""
    mayor = -1
    if a == b:
        return mayor
    elif a == c:
        return mayor
    elif b == c:
        return mayor
    else:
        if a > b:
            if a > c:
                mayor = a
            else:
                mayor = c
        elif b > c:
            mayor = b
        else:
            mayor = c
    
    return mayor

#programa principal

num1 = int(input("Inserte el primer número: "))
num2 = int(input("Inserte el segundo número: "))
num3 = int(input("Inserte el tercer número: "))

resultado = retornaMayorEstricto(num1, num2, num3)
if resultado != -1:
    print("El mayor estricto es %1d" %resultado)
else:
    print("No existe mayor estricto en los números recibidos")
            
    