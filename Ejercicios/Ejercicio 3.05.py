import random


def creamatriz(f, c):
    filas = f
    butacas_fila = c
    matriz = []
    for f in range(filas):
        matriz.append([0] * butacas_fila)

    return matriz


def cargar_sala(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])

    for f in range(filas):
        for c in range(columnas):
            matriz[f][c] = random.randint(0, 1)


def mostrar_butacas(matriz):
    pass


def reservar(matriz, fila_elegida, butaca_elegida):
    disponible = True
    if matriz[fila_elegida-1][butaca_elegida - 1] != 0:
        disponible = False

    return disponible


def butacas_libres(matriz):
    count = 0
    filas = len(matriz)
    columnas = len(matriz[0])

    for f in range(filas):

        for c in range(columnas):

            if matriz[f][c] == 0:
                count += 1

    return count


def butacas_contiguas(matriz):
    contiguas = 0
    filas = len(matriz)
    columnas = len(matriz[0])

    for f in range(filas):

        contiguas_fila = 1

        for c in range(1, columnas):
            if matriz[f][c] == 0 and matriz[f][c] == matriz[f][c-1]:
                contiguas_fila += 1
                
                if contiguas_fila > contiguas:
                    contiguas = contiguas_fila
                    
            else:
                
                contiguas_fila = 1

    return contiguas


def imprimirmatriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" % elemento, end="")
        print()


# programa principal

mi_matriz = creamatriz(5, 10)
imprimirmatriz(mi_matriz)
print()
cargar_sala(mi_matriz)
imprimirmatriz(mi_matriz)
print()
libres = butacas_libres(mi_matriz)
print("En este momento, hay %d butacas libres" % libres)
print()
contiguas = butacas_contiguas(mi_matriz)
print("La mayor cantidad de butacas contiguas libres son: %d" % contiguas)
print()
fila_elegida = int(
    input("Ingrese la fila elegida en nro. (A=1, B=2, C=3, D=4, E=5): "))

asiento_elegido = int(
    input("Ingrese la butaca elegida: "))

while not reservar(mi_matriz, fila_elegida, asiento_elegido):
    print("El asiento está ocupado, lo sentimos. Elija nuevamente")
    fila_elegida = int(
        input("Ingrese la fila elegida en nro. (A=1, B=2, C=3, D=4, E=5): "))

    asiento_elegido = int(
        input("Ingrese la butaca elegida: "))

print()
print("El asiento está disponible.")
