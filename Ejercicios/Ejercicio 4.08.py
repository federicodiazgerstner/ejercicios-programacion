def ordenastring(str):
    stringlist = str.split()
    stringlist.sort()
    stringordenado = " ".join(stringlist)
    
    return stringordenado


#programa principal
mi_string = input("Inserte un string: ")
print(mi_string)
ordenado = ordenastring(mi_string)
print(ordenado)
    