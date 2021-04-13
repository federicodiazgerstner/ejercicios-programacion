def muestra_listado(pac, urg):
    """Imprime listado de pacientes, ordenados según tipo de consulta"""
    print()
    for i in range(len(pac)):
        if urg[i] == 0:
            print("Urgencia - Paciente Nro: %d" % pac[i])

    print()
    for j in range(len(pac)):
        if urg[j] == 1:
            print("Turno - Paciente Nro: %d" % pac[j])

    return


def imprime_consulta_individual(nropac, pac, urg):
    """Recibe el número de afiliado y devuelve número de consultas de urgencia y por turno"""
    print("Consultas del afiliado Nro.: %d " % nropac)
    nro_turnos = 0
    nro_urgencias = 0

    for k in range(len(urg)):
        if pac[k] == nropac:
            if urg[k] == 0:
                nro_urgencias += 1
            else:
                nro_turnos += 1

    print("-Turnos: %d" % nro_turnos)
    print("-Urgencias: %d" % nro_urgencias)

    return


# programa principal
pacientes = []
urgencias = []

nro_paciente = int(
    input("Ingrese el número de afiliado (-1 para finalizar): "))

while nro_paciente != -1:
    tipo_consulta = int(
        input("Ingrese 0 si es urgencia, o 1 si tiene turno: "))

    pacientes.append(nro_paciente)
    urgencias.append(tipo_consulta)

    nro_paciente = int(
        input("Ingrese el número de afiliado (-1 para finalizar): "))


print("Listado de pacientes atentidos, según consulta: ")
muestra_listado(pacientes, urgencias)
print()

paciente_buscado = int(
    input("Ingrese el número de afiliado del paciente a buscar: "))
print()

if paciente_buscado not in pacientes:
    print("El paciente no se ha atendido nunca.")
else:
    imprime_consulta_individual(paciente_buscado, pacientes, urgencias)
