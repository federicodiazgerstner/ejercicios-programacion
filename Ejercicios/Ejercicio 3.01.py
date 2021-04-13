def creamatriz(n):
    matriz = []
    filas = n
    columnas = n
    
    for i in range(filas):
        matriz.append([0] * columnas)
        
    return matriz

def imprimirmatriz(matriz):
    "Otra manera de imprimirla, sin subíndices, solo para lectura"
    for fila in matriz:
        for elemento in fila:
            print("%3d" %elemento, end="")
        print()

def cargamatriz(matriz): #a) cargar matriz con numero.
    for i in range (len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] =  int(input("Ingrese un número: "))
    
    return


def ordenafila(matriz): #ordena todas las filas de la matriz en forma ascendente
    for i in range(len(matriz)):
        matriz[i].sort()


def intercambiarfilas(matriz, a, b): #intercambia dos filas de una matriz que se reciben como parámetro (index comienza en 0)
    aux = matriz[a][:]
    matriz[a] = matriz[b][:]
    matriz[b] = aux[:]
    

def intercambiarcolumnas(matriz, a, b): #intercambia dos columnas de una matriz, recibidas como parámetro (index comienza en 0)
    for i in range(len(matriz)):
        aux = matriz[i][a]
        matriz[i][a] = matriz[i][b]
        matriz[i][b] = aux

def trasponermatriz(matriz): #traspone la matriz sobre sí misma
    filas = len(matriz)
    columnas = len(matriz[0])
    inicio = 0
    for i in range(inicio, filas):
        for j in range(inicio, columnas):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
        
        inicio += 1


def calculapromedio_fila(matriz, fila): #calcula el promedio de una fila una matriz recibida como parámetro
    suma = 0
    
    for pos in matriz[fila]:
        suma += pos
    
    promedio = suma / len(matriz[fila])
    
    return promedio
    

def porcentaje_impares_columna(matriz, columna): #calcula el porcentaje de nros impares en una columna recibida como parámetro
    cant_impares = 0
    for i in range(len(matriz)):
        if matriz[i][columna] % 2 != 0:
            cant_impares += 1
    
    porcentaje = cant_impares / len(matriz[0]) * 100
    
    return porcentaje


def essimetrica(matriz): #determina si la matriz es simétrica respecto de la diagonal principal
    simetrica  = True
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if i == j:
                continue
            elif matriz[i][j] != matriz[j][i]:
                simetrica = False
    
    return simetrica
            


def essimetrica_secundaria(matriz): #determina si la matriz es simetrica respecto de la diagonal secundaria
    simetricasec = True
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        for j in range(columnas):
            if i+j == filas+1:
                continue
            
            elif matriz[i][j] != matriz[-(j+1)][-(i+1)]:
                simetricasec = False
    
    return simetricasec

def espalindromo(matriz): #determina qué columnas son palíndromos y devuelve una lista con los números en ellas.
    columnas_pal = []
    lista_palindromos = []

    largo = len(matriz)
    for i in range(largo):
        palindromo  = True
        for j in range(largo):
            if matriz[j][i] != matriz[-(j+1)][i]:
                palindromo = False
            
        if palindromo:
            columnas_pal.append(i)
            for k in range(largo):
                lista_palindromos.append(matriz[k][i])

    
    return columnas_pal, lista_palindromos
    
        


#programa principal
mi_matriz = [[4,3,4,1],[4,3,4,2],[4,3,4,3],[1,3,4,4]]
# mi_matriz = [[1,2,3,4],[2,1,3,4],[3,3,1,4],[4,4,4,1]]
print("Matriz original: ")
imprimirmatriz(mi_matriz)
# print()
# # cargamatriz(mi_matriz)
# # print("Matriz cargada: ")
# ordenafila(mi_matriz)
# print("Matriz ordenada: ")
# imprimirmatriz(mi_matriz)
# print()
# intercambiarcolumnas(mi_matriz, 1, 2)
# print("Matriz intercambiada:")
# imprimirmatriz(mi_matriz)
# print()
# trasponermatriz(mi_matriz)
# print("Matriz transpuesta: ")
# imprimirmatriz(mi_matriz)
# print()
# columna = int(input("Ingrese la columna de la cual desea saber el promedio: "))
# print(f"Promedio de la fila {columna}: ", end="")
# print(calculapromedio_fila(mi_matriz, columna))
# print()
# columna_impares = int(input("Ingrese la columna de la cual desea saber el porcentaje de impares: "))
# print(f"Porcentaje de impares de columna {columna_impares}: ", end="")
# print(porcentaje_impares_columna(mi_matriz, columna_impares))

if essimetrica(mi_matriz):
    print("La matriz es simétrica respecto de la diagonal principal")
else:
    print("La matriz no es simétrica respecto de la diagonal principal")
    
if essimetrica_secundaria(mi_matriz):
    print("La matriz es simétrica respecto de la diagonal secundaria")
else:
    print("La matriz no es simétrica respecto de la diagonal secundaria")

print()
columnas_palindromo, numeros_palindromos = espalindromo(mi_matriz)

if len(columnas_palindromo) == 0:
    print("Ninguna columna es palíndromo")
else:
    print(f"Las columnas palíndromo son: {columnas_palindromo}")
    print(f"Están compuestas por los números: {numeros_palindromos}")


        