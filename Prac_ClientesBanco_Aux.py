


"""ESTUDIANTE: CONDORI CHOQUE JOSE DANIEL
   CI: 13277399LP"""



#TODO: mockups
clientesNombres = ["Jose","Daniel","Carlos","Felipe","Cesar"]
clientesApellidos = ["Condori","Choque","Ticona","Layme","Apaza"]
clientesCI = ["13277399","1234567","15463287","48796415","48791254"]
clientesFechaNacimiento = [1998, 1999, 1995, 1997, 1996]
clientesTelefono = ["65691484","69845879", "71248556", "65697814","64697814"]
clientesTarjeta = ["6234875691246647", "4759123469124975", "41246971315436197", "45136147894513625", "47812346951246328"]
montoCuenta = [1562, 2800, 900, 120, 3560]
montoDolar = [700, 0, 1500, 0, 0]
clienteDireccion = ["La Paz, Miraflores", "La Paz, Villa Fatima", "El Alto, Ballivian", "El Alto, C.Satelite", "Cochabamba, Sacaba"]

DclientesNombres = []
DclientesApellidos = []
DclientesCI = []
DclientesFechaNacimiento = []
DclientesTelefono = []
DclientesTarjeta = []
DmontoCuenta = []
DmontoDolar = []
DclienteDireccion = []

def mostrarmenu():
    print("")
    print("Igrese la opcion requerida: ")
    print("1. Registrar Cliente: ")
    print("2. Modificar Informacion: ")
    print("3. Habilitar/Deshabilitar Cliente: ")
    print("4. Mostrar Habilitados/Deshabiltados:  ")
    print("5. Despositar/Retirar Monto: ")
    print("6. Calcula Millas: ")
    print("7. Probabilidad de Ganar Sorteo: ")
    print("8. Mostar Monto de Cliente")
    print("0. Salir")
    print("----->")

def registraCliente():
    #Nombres
    nuevonombre=input("Ingrese los Nombres del Cliente: ")
    clientesNombres.append(nuevonombre)
    #Apellidos
    clientesApellidos.append(input("Ingrese los Apellidos del Cliente: "))
    #CI
    clientesCI.append(input("Ingrese el CI del Cliente: "))
    #Fecha Nacimiento
    clientesFechaNacimiento.append(input("Ingrese la Fecha de Nacimiento: "))
    #Telefono
    clientesTelefono.append(input("Ingrese Telefono del Cliente: "))
    #Numero de Tarjeta
    clientesTarjeta.append(input("Ingrese Numero de Tarjeta, Si no Cuenta Con tarjeta Ingrese cero: "))
    #ClienteDireccion
    clienteDireccion.append((input("Ingrese Direccion Del Cliente: ")))
    #MontoCuenta
    montoCuenta.append("0")
    print("Se han guardado los datos")

def ARMonto():
    while True:
        print("1. Depositar Monto:")
        print("2. Retirar Monto:")
        print("0. Salir")

        x=input()
        if x == "1":
            ci = input("Ingrese el CI del Cliente: ")
            if ci in clientesCI:
                while True:
                    print("1. Depositar Bolivianos")
                    print("2. Depositar Dolares")
                    print("0. Salir")
                    y = input()

                    if y == "1":
                        posicion = clientesCI.index(ci)
                        print(f"Saldo Actual: {montoCuenta[posicion]}Bs. ")
                        mon = int(input("Ingrese el Monto a Despositar: "))
                        montoCuenta[posicion] = montoCuenta[posicion] + mon

                        print(f"Saldo Actual {montoCuenta[posicion]}Bs. ")
                    elif y == "2":
                        posicion = clientesCI.index(ci)
                        print(f"Saldo Actual: {montoDolar[posicion]}$us. ")
                        mon = int(input("Ingrese el Monto a Despositar: "))
                        montoDolar[posicion] = montoDolar[posicion] + mon

                        print(f"Saldo Actual {montoDolar[posicion]}$us. ")
                    elif y == "0":
                        break

            else:
                print("El CLiente esta Deshabilitado o no esta Registrado")

        elif x == "2":
            ci = input("Ingrese el CI del Cliente: ")
            if ci in clientesCI:
                while True:
                    print("1. Retirar Bolivianos")
                    print("2. Retirar Dolares")
                    print("0. Salir")
                    y = input()

                    if y == "1":
                        posicion = clientesCI.index(ci)
                        print(f"saldo Actual {montoCuenta[posicion]}Bs.")
                        mon = int(input("Ingrese el Monto a Retirar: "))
                        if mon <= montoCuenta[posicion]:
                            montoCuenta[posicion] = montoCuenta[posicion] - mon
                            print(f"Saldo Actual {montoCuenta[posicion]}Bs.")
                        else:
                            print("Saldo Insuficiente")
                    elif y == "2":
                        posicion = clientesCI.index(ci)
                        print(f"saldo Actual {montoDolar[posicion]}$us.")
                        mon = int(input("Ingrese el Monto a Retirar: "))
                        if mon <= montoDolar[posicion]:
                            montoDolar[posicion] = montoDolar[posicion] - mon
                            print(f"Saldo Actual {montoDolar[posicion]}$us.")
                        else:
                            print("Saldo Insuficiente")



            else:
                print("El cliente esta Deshabilitado o no esta Registrado")
        elif x == "0":
            break





def HDCliente():
    while True:
        print("1. Habilitar")
        print("2. Deshabilitar")
        print("0. Salir")
        print("------>")

        x = input()
        if  x == "1":
            ci = input("Introduzca CI Del Cliente")
            if ci in clientesCI:
                print("El Cliente esta Habilitado \n")
            else:
                if ci in DclientesCI:
                    posicion = DclientesCI.index(ci)
                    clientesNombres.append(DclientesNombres[posicion])
                    clientesApellidos.append(DclientesApellidos[posicion])
                    clientesCI.append(DclientesCI[posicion])
                    clientesFechaNacimiento.append(DclientesFechaNacimiento[posicion])
                    clientesTelefono.append((DclientesTelefono[posicion]))
                    clientesTarjeta.append(DclientesTarjeta[posicion])
                    montoCuenta.append(DmontoCuenta[posicion])
                    clienteDireccion.append((DclienteDireccion[posicion]))
                    montoDolar.append(DmontoDolar[posicion])
                    print(f"Se Habilito al Cliente: {DclientesNombres[posicion]} {DclientesApellidos[posicion]} con CI: {DclientesCI[posicion]} \n")

                    #ELIMINA DE DESHABILITADOS
                    DclientesNombres.pop(posicion)
                    DclientesApellidos.pop(posicion)
                    DclientesCI.pop(posicion)
                    DclientesFechaNacimiento.pop(posicion)
                    DclientesTelefono.pop(posicion)
                    DclientesTarjeta.pop(posicion)
                    DmontoCuenta.pop(posicion)
                    DclienteDireccion.pop(posicion)
                    DmontoDolar.pop(posicion)

                else:
                    print("El Cliente no Existe \n")


        elif x == "2":
            ci = input("Introduzca CI Del Cliente")
            if ci in DclientesCI:
                print("El Cliente esta Deshabilitado \n")
            else:
                if ci in clientesCI:
                    posicion = clientesCI.index(ci)
                    DclientesNombres.append(clientesNombres[posicion])
                    DclientesApellidos.append(clientesApellidos[posicion])
                    DclientesCI.append((clientesCI[posicion]))
                    DclientesFechaNacimiento.append(clientesFechaNacimiento[posicion])
                    DclientesTelefono.append(clientesTelefono[posicion])
                    DclientesTarjeta.append(clientesTarjeta[posicion])
                    DmontoCuenta.append(montoCuenta[posicion])
                    DclienteDireccion.append((clienteDireccion[posicion]))
                    DmontoDolar.append(montoDolar[posicion])
                    print(f"Se Deshabilito al Cliente: {clientesNombres[posicion]} {clientesApellidos[posicion]} con CI: {clientesCI[posicion]} \n")

                    #ELIMINA DE HABILITADOS
                    clientesNombres.pop(posicion)
                    clientesApellidos.pop(posicion)
                    clientesCI.pop(posicion)
                    clientesFechaNacimiento.pop(posicion)
                    clientesTelefono.pop(posicion)
                    clientesTarjeta.pop(posicion)
                    montoCuenta.pop(posicion)
                    clienteDireccion.pop(posicion)
                    montoDolar.pop(posicion)


                else:
                    print("El Cliente no Existe \n")

        elif x == "0":
            break

def mostarHD():
    while True:
        print("Mostrar")
        print("1. Habilitados: ")
        print("2. Deshabilitados: ")
        print("0. Salir")

        x = input()
        if x == "1":
            if len(clientesCI) > 0:
                print("CLIENTES HABILITADOS: ")
                for i in range(len(clientesCI)):
                    print(f"CLIENTE: {clientesNombres[i]} {clientesApellidos[i]} CI: {clientesCI[i]} "
                          f"AÑO DE NACIMIENTO: {clientesFechaNacimiento[i]} TELEFONO: {clientesTelefono[i]}")
            else:
                print("No existen Clientes Habilitados")
        elif x == "2":
            if len(DclientesCI) > 0:
                print("CLIENTES DESHABILITADOS: ")
                for i in range(len(DclientesCI)):
                    print(f"CLIENTE: {DclientesNombres[i]} {DclientesApellidos[i]} CI: {DclientesCI[i]} "
                          f"AÑO DE NACIMIENTO: {DclientesFechaNacimiento[i]} TELEFONO: {DclientesTelefono[i]}")
            else:
                print("No Existen Clientes Deshabilitados")
        elif x == "0":
            break




def modificaCliente():
    ci=input("Introduce el CI del Cliente: ")


    if ci in clientesCI:
         posicion = clientesCI.index(ci)
         while True:
             print("Modificar: ")
             print("1. Direccion")
             print("2. Telefono")
             print("3. Numero De Tarjeta")
             print("4. Salir")
             print("------>")
             x = input()
             if x == "1":
                 print(f"Direccion Actual: {clienteDireccion[posicion]}")
                 mod=input("Ingrese nueva Direccion: ")
                 clienteDireccion[posicion]=mod
                 print("Se Guardo Correctamente \n")
             elif x == "2":
                 print(f"Telefono Actual: {clientesTelefono[posicion]}")
                 mod=input("Ingrese nuevo Telefono: ")
                 clientesTelefono[posicion]=mod
                 print("Se Guardo Correctamente \n")
             elif x == "3":
                 print(f"Numero de Tarjeta Actual: {clientesTarjeta[posicion]}")
                 mod=input("Ingrese nuevo Numero de Tarjeta: ")
                 clientesTarjeta[posicion]=mod
                 print("Se Guardo Correctamente \n")
             elif x == "4":
                 break
    else:
         print(f"El cliente con CI: {ci} no existe")



def caalculaMIlla():
    ci = input("Ingrese el CI de Cliente: ")
    if ci in clientesCI:
        posicion = clientesCI.index(ci)
        if montoDolar[posicion] > 0:
            y = float(input("Ingrese Valor de Entrada: "))
            if y < 1:
                mill = montoDolar[posicion] * y
                print(f"Las Millas de Cliente: {clientesNombres[posicion]} {clientesApellidos[posicion]} CI: {clientesCI[posicion]} es: {mill}")
            else:
                print("Milla mayor a Uno. Error")
        else:
            print("El Cliente no Cuenta con saldo suficiente en Dolares")
    else:
        print("El cliente esta Deshabilitado o no esta Registrado")

def sorteo():
    ci = input("Ingrese el CI del cliente: ")
    if ci in clientesCI:
        posicion = clientesCI.index(ci)
        tiquetTotal = 0
        for i in range(len(clientesCI)):
            if montoCuenta[i] > 99:
                tclientes = montoCuenta[i] // 100
                tiquetTotal = tiquetTotal + tclientes
            else:
                continue

        tcliente = montoCuenta[posicion] // 100

        probabilidad = (tcliente / tiquetTotal)

        print(
            f"La probabilidad de ganar del cliente: {clientesNombres[posicion]} {clientesApellidos[posicion]} es de : {round(probabilidad, 2) * 100}%")

    else:
        print("El cliente esta Deshabilitado o no esta registrado")


def mostarMonto():
    ci = input("Ingrese el CI del Cliente:")

    posicion = clientesCI.index(ci)

    print(f"Saldo de Ciente: {clientesNombres[posicion]} {clientesApellidos[posicion]} es de:")
    print(f"Bolivianos: {montoCuenta[posicion]}bs.  Dolares: {montoDolar[posicion]}$us.")





while True:
    mostrarmenu()
    opcion = input()
    if opcion == "1":
        registraCliente()
    elif opcion == "2":
        modificaCliente()
    elif opcion == "3":
        HDCliente()
    elif opcion == "4":
        mostarHD()
    elif opcion == "5":
        ARMonto()
    elif opcion =="6":
        caalculaMIlla()
    elif opcion == "7":
        sorteo()
    elif opcion == "8":
        mostarMonto()

    else:
        print("Gracias por utilizar el programa")

        break


