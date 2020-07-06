"""Programa con menu
   iniciar una lista de estudiantes
   mostrar lista
   ALTAS
   BAJAS
   MIDIFICACIONES
   Consulta - query
   Consulta2
   Ordenador

   CORE Y REPOSITORIO"""
#TODO: mockups
estudiantesNombres = ["Jose","Daniel","Carlos","Felipe","Cesar"]
estudiantesApellidos = ["Condori","Choque","Ticona","Layme","Apaza"]
estudiantesCI = ["13277399","1234567","15463287","48796415","48791254"]
estudiantesFechaNacimiento = [1998, 1999, 1995, 1997, 1996]
estudiantesTelefono = ["65691484","69845879", "71248556", "65697814","64697814"]

def mostrarmenu():
    print("")
    print("")
    print("Igrese la opcion requerida: ")
    print("1. Mostrar la lista: ")
    print("2. Adicionar un estudiante: ")
    print("3. Modificar Estudiante: ")
    print("4. Eliminar Estudiante: ")
    print("5. Consulta Salida cuarentena: ")
    print("6. Nivel de Riesgo Estudiantes: ")
    print("0. Salir")
    print("----->")

def mostrarestudiantes():
    for i in range(len(estudiantesCI)):
        print(f"ESTUDIANTE: {estudiantesNombres[i]} {estudiantesApellidos[i]} CI: {estudiantesCI[i]} "
              f"AÑO DE NACIMIENTO: {estudiantesFechaNacimiento[i]} TELEFONO: {estudiantesTelefono[i]}")

def adicionarestudiante():
    #Nombres
    nuevonombre=input("ingrese losmnombres del estudiante")
    estudiantesNombres.append(nuevonombre)
    #Apellidos
    estudiantesApellidos.append(input("ingrese los apellidos del estudiante"))
    #CI
    estudiantesCI.append(input("Ingrese el CI del estuiante"))
    #Fecha Nacimiento
    estudiantesFechaNacimiento.append(input("Infrese la fecha de nacimiento"))
    #Telefono
    estudiantesTelefono.append(input("Ingrese telefono del estidiante"))
    print("Se han guardado los datos")

def eliminarestudiante():
    posicion = estudiantesCI.index(input("ingrese eñ ci del estudiante a borrar"))

    estudiantesNombres.pop(posicion)
    estudiantesApellidos.pop(posicion)
    estudiantesCI.pop(posicion)
    estudiantesFechaNacimiento.pop(posicion)
    estudiantesTelefono.pop(posicion)
    print("Se ha eliminado al estudiante correctamente")

# lun mie vie inpares
# mar jue sab pares
#ingresar un dia y mostrar los estudiantes que pueden salir

def consultasalidacuarentena():
    dia=input("Ingrese le dia que desea validar: ")
    comparador = -1
    if dia.lower() in ["lun", "mie", "vie"]:
        comparador=1
        print("los estudiantes que pueden salir son: ")
    elif dia.lower() in ["mar", "jue", "sab"]:
        comparador = 0

    else:
        print("Dia no registrado")
        print("los estudiantes que pueden salir son: ")

    for i in range(len(estudiantesNombres)):
        if int(estudiantesCI[i]) % 2 == comparador:
            print(f"Estudiante: {estudiantesNombres[i]} {estudiantesApellidos[i]} CI: {estudiantesCI[i]} "
                  f"Año de Nacimineto: {estudiantesFechaNacimiento[i]} Telefono: {estudiantesTelefono[i]}")

def modificaestudiante():
    posicion = estudiantesCI.index(input("Introduce el CI del Estudiante: "))
    while True:
        print("Modificar: ")
        print("1. Nombres")
        print("2. Apellidos")
        print("3. CI")
        print("4. Fecha de Nacimiento")
        print("5. Telefono")
        print("6. Salir")
        print("------>")
        x = input()
        if x == "1":
            mod=input("Ingrese nuevo nombre: ")
            estudiantesNombres[posicion]=mod
            print("Se Guardo Correctamente \n")
        elif x == "2":
            mod=input("Ingrese nuevo Apellido: ")
            estudiantesApellidos[posicion]=mod
            print("Se Guardo Correctamente \n")
        elif x == "3":
            mod=input("Ingrese nuevo CI: ")
            estudiantesCI[posicion]=mod
            print("Se Guardo Correctamente \n")
        elif x == "4":
            mod=input("Ingrese nueva Fecha de Nacimiento: ")
            estudiantesFechaNacimiento[posicion]=mod
            print("Se Guardo Correctamente \n")
        elif x == "5":
            mod=input("Ingrese nuevo Telefono: ")
            estudiantesTelefono[posicion]=mod
            print("Se Guardo Correctamente \n")
        elif x == "6":
            break

def risegoestudiantes():
    while True:
        print("ingrese Nivel de Riesgo: ")
        print("1. Riesgo Alto")
        print("2. Riesgo Bajo")
        print("3. Riesgo Medio")
        print("------>")
        x = input()
        if x == "1":
            for i in range(len(estudiantesFechaNacimiento)):
                if 2020 - estudiantesFechaNacimiento[i] > 45:
                    print(f"Estudiante: {estudiantesNombres[i]} {estudiantesApellidos[i]} CI: {estudiantesCI[i]}")
        elif x == "2":
            for i in range(len(estudiantesFechaNacimiento)):
                if 2020 - estudiantesFechaNacimiento[i] > 0 and 2020 - estudiantesFechaNacimiento[i] < 26:
                    print(f"Estudiante: {estudiantesNombres[i]} {estudiantesApellidos[i]} CI: {estudiantesCI[i]}")
        elif x == "3":
            for i in range(len(estudiantesFechaNacimiento)):
                if 2020 - estudiantesFechaNacimiento[i] > 25 and 2020 - estudiantesFechaNacimiento[i] < 46:
                    print(f"Estudiante: {estudiantesNombres[i]} {estudiantesApellidos[i]} CI: {estudiantesCI[i]}")
        else:
            break



while True:
    mostrarmenu()
    opcion = input()
    if opcion == "1":
        print("Esta es la lista de estudiantes registrados: ")
        mostrarestudiantes()
    elif opcion == "2":
        adicionarestudiante()
    elif opcion == "3":
        modificaestudiante()
    elif opcion == "4":
        eliminarestudiante()
    elif opcion == "5":
        consultasalidacuarentena()
    elif opcion =="6":
        risegoestudiantes()
    else:
        print("Gracias por utilizar el programa")

        break



#TAREA RELIZAR EL METODO MODIFICAR DE LAS LISTAS DE ESTUDIANTES
#TAREA2 INVENTAR UNA CONSULTA CUALQUIERA COMO SALIDA CUARENTENA Y PONERLA COMO OPCION 6
#TAREA3 MEJORAR EL DISEÑO EN GENENRAL(ASPECTO) HASTA EL MARTES