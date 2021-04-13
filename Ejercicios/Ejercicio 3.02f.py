def creamatriz(n):
    filas = n
    columnas = n
    matriz = []
    for f in range(filas):
        matriz.append([0] * columnas)

    return matriz


def rellenamatriz(matriz):
    number = 1

    for i in range(0, len(matriz)):  # recorre filas

        counter = 0

        # recorre columnas de última a primera.
        for j in range(-1, -len(matriz)-1, -1):
            matriz[i][j] = number
            counter += 1

            if counter == i+1:
                number += 1
                break

            else:
                number += 1

    return


def imprimirmatriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print("%3d" % elemento, end="")
        print()

# Programa Principal


mi_matriz = creamatriz(4)
rellenamatriz(mi_matriz)
imprimirmatriz(mi_matriz)
