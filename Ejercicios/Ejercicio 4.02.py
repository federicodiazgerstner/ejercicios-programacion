string = input("Inserte una cadena de caracteres: ")
longitud = len(string)
lados = int((80 - longitud)/2)

print(" " * lados + string + " " * lados)