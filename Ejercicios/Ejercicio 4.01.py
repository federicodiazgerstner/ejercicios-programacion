def es_capicua(s):
    capicua = True
    for i in range(len(s)):
        if s[i] != s[-(i+1)]:
            capicua = False
            break
    
    return capicua

#programa principal

mi_string = input("Inserte un string: ")

if es_capicua(mi_string):
    print("La cadena es capicua.")
else:
    print("La cadena no es capicua.")
            