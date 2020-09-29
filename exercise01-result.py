listaRegistro = []
costoTotal = 0


def iniciar():
    global costoTotal

    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))

    costoTotal = costoTotal + costo

    registro = dict(cliente=cliente, producto=producto, costo=costo)
    listaRegistro.append(registro)

    print("oprima 1 si quiere añadir otro registro")
    print("oprima 2 si quiere parar")
    opcion = int(input(""))

    if opcion == 1:
        iniciar()
    elif opcion == 2:
        print("")
        print("el costo total es: ")
        print(costoTotal)


iniciar()
