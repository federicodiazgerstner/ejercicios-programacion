def creabaraja():
    baraja = []
    oros = [f"{x} Oros" for x in range(1,13)]
    bastos = [f"{x} Bastos" for x in range(1,13)]
    espadas = [f"{x} Espadas" for x in range(1,13)]
    copas = [f"{x} Copas" for x in range(1,13)]
    
    baraja = oros + bastos + espadas + copas
    
    return baraja

#programa principal

print(creabaraja())
