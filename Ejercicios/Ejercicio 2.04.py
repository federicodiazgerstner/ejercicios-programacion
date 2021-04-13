def imprimelista(list):
    for i in range (len(list)):
        print(list[i], end="  ")

def eliminaValores(list, remove):
    newList = []
    
    for i in range(len(list)):
        if list[i] not in remove:
            newList.append(list[i])
            
    return newList
            

#programa principal

lista = ["Melman", "Gloria", "Martin", "Alex"]
print("Lista original:")
imprimelista(lista)
print()
print()
eliminar = ["Melman","Martin"]
print("Palabras a eliminar:")
imprimelista(eliminar)
print()
print()


print("Lista resultante:")
imprimelista(eliminaValores(lista, eliminar))
