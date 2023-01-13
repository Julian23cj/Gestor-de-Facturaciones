def menu_principal():
    print("------Menu Inicial------\n"
    "1- Buscar Facturaciones.\n"
    "2- Crear nueva Facturación.\n"
    "3- Modificar Facturaciones.\n"
    "4- Eliminar Facturaciones.\n"
    "5- Salir.\n")
    opcion=control_de_errores()
    return opcion

def menu_buscar_facturaciones():
    print("------Menu Busqueda Facturaciones------\n"
    "1- Mostrar todas las facturaciones.\n"
    "2- Mostrar ultimas 10 facturaciones.\n"
    "3- Buscar facturación por direccción.\n"
    "4- Buscar facturación por cuil.\n"
    "5- Buscar facturación por fecha.\n"
    "6- Volver al menu inicial.\n")
    opcion=control_de_errores()
    return opcion

def control_de_errores():
    while True:
        entrada=input("ingrese una opción: ")
        try:
            entrada=int
            return entrada
        except:
            print("Error, ingrese un numero.\n")
