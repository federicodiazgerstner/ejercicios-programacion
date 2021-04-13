def diasiguiente(d, m, a):
    if d+1 == 31: #determina el día siguiente y el cambio de mes de ser necesario.
        if (m == 4 or m == 6 or m == 9 or m == 11):
            d = 1
            m += 1
        else:
            d +=1
    elif (d+1 == 29 and m == 2):
        d = 1
        m += 1
    elif (d+1 == 32):
        d = 1
        if m == 12:
           m = 1
           a += 1
        else:
           m += 1
    else:
        d += 1
    
    
    return d, m, a


# #programa principal a)
#
# dia = int(input("Inserte el dia: "))
# mes = int(input("Inserte el mes: "))
# año = int(input("Inserte el año: "))
# n = int(input("Ingrese cantidad de días a sumar a la fecha: "))
# 
# while n > 0:
#     dia, mes, año = diasiguiente(dia, mes, año)
#     n -= 1
#     
# print("Luego de sumar ", n, " días a la fecha inicial, llegamos a la fecha: %2d / %2d / %4d" %(dia, mes, año))


#programa principal b)

fecha1_dia = int(input("Inserte el día de la primer fecha: "))
fecha1_mes = int(input("Inserte el mes de la primer fecha: "))
fecha1_año = int(input("Inserte el año de la primer fecha: "))

fecha2_dia = int(input("Inserte el día de la segunda fecha: "))
fecha2_mes = int(input("Inserte el mes de la segunda fecha: "))
fecha2_año = int(input("Inserte el año de la segunda fecha: "))

contador = 0
    
while ((fecha1_dia != fecha2_dia) or (fecha1_mes != fecha2_mes) or (fecha1_año != fecha2_año)):
    fecha1_dia, fecha1_mes, fecha1_año = diasiguiente(fecha1_dia, fecha1_mes, fecha1_año)
    contador += 1

print("La cantidad de días entre la primer fecha y la segunda fecha son: %5d días" %contador)
    
    
        