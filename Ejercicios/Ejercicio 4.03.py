def desencriptar(clave):
    str_clave = str(clave)
    str_clave1= ''
    str_clave2 = ''
    
    for i in range(len(str_clave)):
        if (i+1)% 2 != 0:
            str_clave1 += str_clave[i]
        else:
            str_clave2 += str_clave[i]
    
    clave1 = int(str_clave1)
    clave2 = int(str_clave2)
    
    return clave1, clave2

#programa principal

password = 5546421657435876468413

pass1, pass2 = desencriptar(password)
print("Clave 1: %d" %pass1)
print("Clave 2: %d" %pass2)