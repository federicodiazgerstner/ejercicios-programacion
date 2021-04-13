def extraer_string(cadena, pos, num):
    nueva_string = ''
    for i in range(pos, pos+num):
        nueva_string += cadena[i]
    
    return nueva_string


def extraer_rebanada(cadena, pos, num):
    nueva_string = cadena[pos:pos+num]
    
    return nueva_string
    
#programa principal

mi_string = input("Ingrese una cadena de la cual se extraerá una subcadena: ")
posicion = int(input("Inserte la posicion de inicio: "))
longitud = int(input("Inserte la cantidad de caracteres a extraer: "))

string_extraida = extraer_string(mi_string, posicion, longitud)

print(string_extraida)

