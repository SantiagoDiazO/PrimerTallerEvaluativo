opcionActual = 999
ciclistas = []

print("***CICLISTAS***")
print("1: Registrar ciclista")
print("2: Ver tabla posiciones")
print("3: Corregir tiempo ciclista")
print("4: Eliminar cilista")
print("0: Salir")

codigoCiclista = 1

while opcionActual != 0:
    opcionActual = int(input("Digite la opcion deseada: "))
    if opcionActual == 1:
        ciclista = {}
        ciclista["codigo"] = codigoCiclista
        print(f'El codigo del ciclista es: {codigoCiclista}')
        ciclista["nombre"] = input("Ingrese el nombre del ciclista: ")
        ciclista["edad"] = int(input("Ingrese la edad del ciclista: "))
        ciclista["pais"] = input("Ingrese el pais del que proviene el ciclista: ")
        ciclista["equipo"] = input("Ingrese el equipo al que pertenece el ciclista: ")
        ciclista["tiempo"] = int(input("Ingrese el tiempo del ciclista en minutos: "))
        ciclistas.append(ciclista)
        codigoCiclista += 1
        print("Ciclista registrado correctamente")
    elif opcionActual == 2:
        ordenCiclistas = 1
        for mostrarCiclista in ciclistas:
            print(ordenCiclistas)
            print(f'Codigo: {mostrarCiclista["codigo"]}')
            print(f'Nombre: {mostrarCiclista["nombre"]}')
            print(f'Edad: {mostrarCiclista["edad"]}')
            print(f'Pais: {mostrarCiclista["pais"]}')
            print(f'Equipo: {mostrarCiclista["equipo"]}')
            print(f'Tiempo: {mostrarCiclista["tiempo"]}')
            ordenCiclistas += 1
    elif opcionActual == 3:
        codigoABuscar = int(input("Ingrese el codigo del ciclista para corregir: "))
        for ciclistaABuscar in ciclistas:
            if ciclistaABuscar["codigo"] == codigoABuscar:
                ciclistaABuscar["tiempo"] = int(input("Ingrese el nuevo tiempo del ciclista: "))
                print("Tiempo cambiado correctamente")
            else:
                print("No se encontro el codigo del ciclista")
    elif opcionActual == 4:
        codigoABuscar = int(input("Ingrese el codigo del ciclista para eliminar: "))
        for ciclistaABuscar in ciclistas:
            if ciclistaABuscar["codigo"] == codigoABuscar:
                ciclistas.remove(ciclistaABuscar)
                print("Ciclista eliminado correctamente")
            else:
                print("No se encontro el codigo del ciclista")
    elif opcionActual == 0:
        print("Hasta luego")
        break
    else:
        print("Digite una opcion valida")