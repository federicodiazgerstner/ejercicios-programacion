def encuentra_substring(string, substring):
    cantidad = 0
    substr = ""
    
    for i in range(len(string)):
        for letra in substring:
            if string[i] == letra and string[i] not in substr:
                substr += string[i]
            
            if substr == substring:
                cantidad += 1
    
    return cantidad

#programa principal

cadena = input("Ingrese una cadena: ")
subs = input("Ingrese la subcadena a analizar dentro del string: ")
print(encuentra_substring(cadena, subs))