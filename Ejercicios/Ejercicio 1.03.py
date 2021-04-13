def calculaGastos(cant, valor):
    """Toma la cantidad de viajes realizados en transporte junto con el valor actualizado, y calcula cuánto
se gastó en un mes"""
    gastos_rango3 = 0
    gastos_rango2 = 0
    gastos_rango1 = 0
    gastos_rango0 = 0
    while cant > 0:
        if cant > 40:
            gastos_rango3 = (cant - 40) * valor * 0.6
            cant -= (cant-40)
        elif cant > 30:
            gastos_rango2 = (cant - 30) * valor * 0.7
            cant -= (cant-30)
        elif cant > 20:
            gastos_rango2 = (cant - 20) * valor * 0.8
            cant -= (cant-20)
        else:
            gastos_rango0 = cant * valor
            cant -= cant
    gasto_total = gastos_rango3 + gastos_rango2 + gastos_rango1 + gastos_rango0
    
    return gasto_total

#programa principal

cant_viajes = int(input("Inserte la cantidad de viajes realizados/a realizar en el mes: "))
tarifa = float(input("Inserte la tarifa actualizada de un viaje: "))
total = calculaGastos(cant_viajes, tarifa)

print("El total de gastos realizados/a realizar es de %5.2f" %total)