import random

def creamatriz(n):
    matriz = []
    filas = n
    columnas = n
    
    for f in range(filas):
        matriz.append([0] *columnas)
    
    return matriz

def rellena_matriz(matriz):
    largo = len(matriz)
    numbers = []
    
    while len(numbers) < largo**2:
        
        for i in range(largo):
            for j in range(largo):
                repetido = True
                
                while repetido:
                    num =  random.randint(0, largo**2 - 1)
                    
                    if num not in numbers:
                        numbers.append(num)
                        repetido = False
                        
                if matriz[i][j] == 0:
                    matriz[i][j] = num

        
        
    return

def imprimirmatriz(matriz):
    "Otra manera de imprimirla, sin subíndices, solo para lectura"
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

#programa principal
length = int(input("Ingrese el largo: "))
mi_matriz = creamatriz(length)
imprimirmatriz(mi_matriz)
print()
rellena_matriz(mi_matriz)
imprimirmatriz(mi_matriz)
