def diadelasemana(dia,mes,año):
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (((26*mes-2)//10)+dia+año2+(año2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

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

#programa principal
dia = 1
mes = int(input("Inserte un mes: "))
año = int(input("Inserte un año: "))

if mes == 12:
    aux = 1
else:
    aux = mes + 1

while mes != aux:
    nombre_dia = diadelasemana(dia, mes, año)
    if nombre_dia == 0:
        print("Domingo %d de %02d de %d" % (dia, mes, año))
    elif nombre_dia == 1:
        print("Lunes %d de %02d de %d" % (dia, mes, año))
    elif nombre_dia == 2:
        print("Martes %d de %02d de %d" % (dia, mes, año))
    elif nombre_dia == 3:
        print("Miércoles %d de %02d de %d" % (dia, mes, año))
    elif nombre_dia == 4:
        print("Jueves %d de %02d de %d" % (dia, mes, año))
    elif nombre_dia == 5:
        print("Viernes %d de %02d de %d" % (dia, mes, año))
    else:
        print("Sábado %d de %02d de %d" % (dia, mes, año))
        
    dia, mes, año = diasiguiente(dia, mes, año)


