def filtrar_palabras(f, n):
    frase = f.split(" ")
    palabras = []
    for palabra in frase:
        if len(palabra) >= n:
            palabras.append(palabra)
    
    str = palabras.join(" ")
    
    return str

def filtrar_palabras_comprension(f, n):
    frase = f.split(" ")
    palabras = [palabra for palabra in frase if len(palabra) >= n]
    
    str = palabras.join(" ")
    
    return str

def filtrar_palabras_filter(f, n):
    frase = f.split(" ")
    palabras = list(filter(lambda palabra: len(palabra) >= n, frase))
    
    str = palabras.join(" ")
    
    return str

#programa principal
mi_frase = input("Ingrese una frase u oracion: ")
num = int(input("Ingrese un numero limite: "))
p_filtradas = filtrar_palabras_filter(mi_frase, num)

print(p_filtradas)