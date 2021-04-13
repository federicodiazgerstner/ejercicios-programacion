def eliminarsubstring(c, pos, num):
    inicio = 0
    if pos == 0:
        inicio += num
        
    nuevacadena = c[inicio:pos]+c[pos+num:]
    
    return nuevacadena

def eliminar_sinrebanada(c, pos, num):
    nuevacadena = ''
    for i in range(len(c)):
        if i < pos or i>=pos+num:
            nuevacadena += c[i]
    
    return nuevacadena
        
        
#programa principal

mi_cadena = input("Ingrese una cadena objetivo: ")
print(mi_cadena)
posicion = int(input("Ingrese la posición desde la cual eliminar: "))
longitud = int(input("Ingrese la cantidad de caracteres a eliminar: "))
nueva_cadena = eliminar_sinrebanada(mi_cadena, posicion, longitud)
print(nueva_cadena)



