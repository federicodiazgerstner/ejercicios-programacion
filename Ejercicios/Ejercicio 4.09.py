def devuelveultimos(str, n):
    ultimos = str[len(str)-n:]
    
    return ultimos


#programa principal
mi_string = input("Ingrese un string: ")
caracteres = int(input("Ingrese la cantidad de caracteres: "))
print(mi_string)
ultimos_car = devuelveultimos(mi_string, caracteres)
print(ultimos_car)
                