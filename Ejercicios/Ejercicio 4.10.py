def limpiarpalabra(palabra):
    i=0
    while i < len(palabra) and not palabra[i].isalpha():
        i+=1
    inicio=palabra[:i]
    j=len(palabra)-1
    while j>i and not palabra[j].isalpha():
        j-=1
    final=palabra[j+1:]
    palabra=palabra[i:j+1]
    return inicio, palabra, final
        
        
def reemp(cad, palab, reempalab):
    cadd=cad.split()
    cant=0
    for i in range (len(cadd)):
        prefijo,palabralimpia,sufijo=limpiarpalabra(cadd[i])
        if palabralimpia==palab:
            cadd[i]=prefijo+reempalab+sufijo
            cant+=1
    return ' '.join(cadd), cant
            

cad=input("ingresar cadena de caracteres: ")
palabra=input("ingresar palabra a remplazar:")
reemppalab=input("ingresar palabra de reemplazo: ")
remplazar,cant=reemp(cad,palabra,reemppalab)
print("\n",remplazar,"\n \n Se remplazo %d veces "%(cant))