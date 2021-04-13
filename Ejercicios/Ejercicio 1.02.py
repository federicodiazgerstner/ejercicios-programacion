def esFechaValida(dia, mes, año):
    """Toma parámetros día, mes y año, y verifica que la fecha sea válida"""
    if 1 <= dia <= 31:
        if 1 <= mes <= 12:
            if año > 0:
                return True
    else:
        return False
    
#programa principal
d = int(input("Inserte el día: "))
m = int(input("Inserte el mes: "))
a = int(input("Inserte el año: "))

if esFechaValida(d, m, a):
    print("La fecha es correcta")
else:
    print("La fecha es incorrecta")