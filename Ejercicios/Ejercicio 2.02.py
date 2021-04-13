import random

def randomList():
    """Devuelve una lista con 50 números del 1 al 100"""
    myList = []
    
    while len(myList) < 50:
        myList.append(random.randint(1, 100))
    
    return myList

def isRepeated(list):
    """Chequea si una lista tiene elementos repetidos"""
    repeated = False
    
    for i in range(len(list)):
       if list.count(list[i]) > 1:
           repeated = True
           break
    
    return repeated

def unique(list):
    """Toma una lista y devuelve otra con los elementos únicos"""
    newList = []
    
    for i in range(len(list)):
        if list.count(list[i]) == 1:
            newList.append(list[i])
    
    return newList


#programa principal


lista = randomList()

print("Generamos una lista: ")
print()
print(lista, end=" ")
print()
print()
print("Comprobando si tiene elementos repetidos...")
print()

tieneRepetidos = isRepeated(lista)

if tieneRepetidos:
    print("Sí. Tiene elementos repetidos.")
    print("Depurando la lista...")
    nuevaLista = unique(lista)
    print()
    print("La lista nueva con valores únicos es: ")
    print()
    print(nuevaLista, end=" ")
    print()
else:
    print("No tiene elementos repetidos")

print()
print("Fin")

           
    