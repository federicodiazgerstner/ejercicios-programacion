import random

def crearmatriz(n): #crea matriz de N x N
    matriz = []
    filas = n
    columnas = 7
    
    for i in range(filas):
        matriz.append([0] * columnas)
        
    return matriz


def rellenarmatriz(matriz): #rellena matriz con números random.
    
    filas = len(matriz)
    columnas = len(matriz[0])
    
    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(0,150)


def devuelve_totales(matriz): #devuelve una list con los totales de cada fábrica
    totales = []
    
    for i in range(len(matriz)):
        totales.append(sum(matriz[i]))
    
    return totales


def fabprod(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    max = 0
    fabrica = 0
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    dia = ""
    for f in range(filas):
        for c in range(columnas):
            if matriz[f][c] > max:
                max = matriz[f][c]
                fabrica = f+1
                dia = dias[c]
    
    return fabrica, dia

def diaprod(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    dias = [0,0,0,0,0,0,0]
    
    for f in range(filas):
        for c in range(columnas):
            dias[c] += matriz[f][c]
            
    diamax = max(dias)
    
    
    return dias.index(diamax)
            
def imprimirmatriz(matriz):
    "Otra manera de imprimirla, sin subíndices, solo para lectura"
    for fila in matriz:
        for elemento in fila:
            print("%6d" %elemento, end="")
        print()
                

    
#programa principal
n = int(input("Ingrese el número de la matriz cuadrada: "))
mimatriz = crearmatriz(n)
rellenarmatriz(mimatriz)
imprimirmatriz(mimatriz)
print()

prodtotal = devuelve_totales(mimatriz)

for i in range(len(prodtotal)):
    total = prodtotal[i]
    print(f"La fábrica {i+1} produjo {total} bicicletas")
print()

fab, diaproduc = fabprod(mimatriz)
print(f"La fábrica {fab} produjo la mayor cantidad de unidades en el día {diaproduc}")
print()

diamaxprod = diaprod(mimatriz)
print(f"El dia de mayor producción fue el día {diamaxprod+1}")

            
