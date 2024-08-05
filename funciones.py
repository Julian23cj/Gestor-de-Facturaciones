import os
import base_de_datos as bd

def crear_base_datos():
    con, cur= bd.conectar()
    bd.crear_tabla(con, cur)

def menu_principal():
    print("------Menu Inicial------\n"
    "1- Buscar Facturaciones.\n"
    "2- Crear nueva Facturación.\n"
    "3- Modificar Facturaciones.\n"
    "4- Eliminar Facturaciones.\n"
    "5- Salir.\n")
    opcion=control_de_entrada_usuario()
    return opcion

def menu_buscar_facturaciones():
    print("------Menu Busqueda Facturaciones------\n"
    "1- Mostrar todas las facturaciones.\n"
    "2- Mostrar ultimas 10 facturaciones.\n"
    "3- Buscar facturación por fecha.\n"
    "4- Buscar facturación por cuil.\n"
    "5- Buscar facturación por direccion.\n"
    "6- Volver al menu inicial.\n")
    opcion=control_de_entrada_usuario()
    return opcion



#Busqueda de facturas

def todas_facturaciones():
    con,cur=bd.conectar()
    cur.execute('SELECT * FROM Facturaciones')
    datos=cur.fetchall()
    
    for fila in datos:
        print(f'Número de Facturación: {fila[1]} CUIL: {fila[2]} Dirección: {fila[3]} Fecha: {fila[4]}/{fila[5]}/{fila[6]} Importe: {fila[7]} Descripción: {fila[8]}')
        print('---')
    con.close()

def ultimas_dies_facturaciones():
    con,cur=bd.conectar()
    cur.execute(f'SELECT * FROM Facturaciones ORDER BY N°FACTURACION DESC LIMIT 10')
    datos=cur.fetchall()

    for fila in datos:
        print(f'Número de Facturación: {fila[1]} CUIL: {fila[2]} Dirección: {fila[3]} Fecha: {fila[4]}/{fila[5]}/{fila[6]} Importe: {fila[7]} Descripción: {fila[8]}')
        print('---')
    con.close()

def buscar_fac_fecha_mes():
    con,cur=bd.conectar()
    mes=control_mes()
    cur.execute(f'SELECT * FROM Facturaciones WHERE MES = {mes}')
    datos=cur.fetchall()

    for fila in datos:
        print(f'Número de Facturación: {fila[1]} CUIL: {fila[2]} Dirección: {fila[3]} Fecha: {fila[4]}/{fila[5]}/{fila[6]} Importe: {fila[7]} Descripción: {fila[8]}')
        print('---')
    con.close()

def buscar_fac_cuil():
    con,cur=bd.conectar()
    cuil=control_cuil()
    cur.execute(f'SELECT * FROM Facturaciones WHERE CUIL = {cuil}')
    datos=cur.fetchall()

    for fila in datos:
        print(f'Número de Facturación: {fila[1]} CUIL: {fila[2]} Dirección: {fila[3]} Fecha: {fila[4]}/{fila[5]}/{fila[6]} Importe: {fila[7]} Descripción: {fila[8]}')
        print('---')
    con.close()

def buscar_fac_direccion():
    con,cur=bd.conectar()
    direccion=input("Ingresa la dirección: ")
    cur.execute('''SELECT * FROM Facturaciones WHERE DIRECCION LIKE ?''',(f'%{direccion}%',))
    datos=cur.fetchall()

    for fila in datos:
        print(f'Número de Facturación: {fila[1]} CUIL: {fila[2]} Dirección: {fila[3]} Fecha: {fila[4]}/{fila[5]}/{fila[6]} Importe: {fila[7]} Descripción: {fila[8]}')
        print('---')
    con.close()

#Creacion de facturas

def crear_facturacion():
    
    while True:
        numeroFac= control_numero_facturacion()
        con,cur=bd.conectar()
        cur.execute('SELECT * FROM Facturaciones')
        datos=cur.fetchall()
        aux=False
        for Nro_fac in datos:
            if numeroFac == Nro_fac[1]:
                print("\033[1;31m"+"Error ya existe una facturación con ese numero.Ingrese el numero nuevamente.\n"+'\033[0;m')
                print("")
                aux=True
                break
            else:
                aux=False
        if aux == True:
            continue
        elif aux== False:
            con.close()
            break
    cuil= control_cuil()
    direccion= str(input("Ingresa la direccion: "))
    print("")
    dia = control_dia()
    mes = control_mes()
    anio= control_anio ()
    importe= control_importe()
    descripcion = (input("Ingresa una descripción: "))
    return numeroFac, cuil, direccion, dia, mes, anio, importe, descripcion

#Control de errores

def control_de_entrada_usuario():
    while True:
        entero=input ('Ingrese una opcion: ')
        try:
            entero=int(entero)
            print("")
            # os.system("cls")
            return entero
        except ValueError:
            print("\033[1;31m"+"Error, ingrese un numero.\n"+'\033[0;m')

def control_numero_facturacion():
    while True:
        entero=input ('Ingresa el numero de facturacion: ')
        try:
            entero=int(entero)
            print("")
            # os.system("cls")
            return entero
        except ValueError:
            print("\033[1;31m"+"Error, ingrese un numero.\n"+'\033[0;m')

def control_cuil():
    while True:
        entero=input ('Ingresa el cuil: ')
        try:
            entero=int(entero)
            print("")
            if entero >= 10000000000 and entero<= 99999999999:
                return entero
            else:
                print("\033[1;31m"+"Error, ingresa un cuil valido.\n"+'\033[0;m')
        except ValueError:
            print("\033[1;31m"+"Error, ingrese un numero.\n"+'\033[0;m')

def control_dia():
    while True:
        entero=input ('Ingresa el día: ')
        try:
            entero=int(entero)
            print("")
            if entero >= 1 and entero<= 31:
                return entero
            else:
                print("\033[1;31m"+"Error, ingresa un día valido.\n"+'\033[0;m')
        except ValueError:
            print("\033[1;31m"+"Error, ingrese un numero.\n"+'\033[0;m')

def control_mes():
    while True:
        entero=input ('Ingresa el mes: ')
        try:
            entero=int(entero)
            print("")
            if entero >= 1 and entero<= 12:
                return entero
            else:
                print("\033[1;31m"+"Error, ingresa un mes valido.\n"+'\033[0;m')
        except ValueError:
            print("\033[1;31m"+"Error, ingrese un numero.\n"+'\033[0;m')

def control_anio():
    while True:
        entero=input ('Ingresa el año: ')
        try:
            entero=int(entero)
            print("")
            if entero >= 2000 and entero<= 4000:
                return entero
            else:
                print("\033[1;31m"+"Error, ingresa un año valido.\n"+'\033[0;m')
        except ValueError:
            print("\033[1;31m"+"Error, ingrese un numero.\n"+'\033[0;m')

def control_importe():
    while True:
        entero=input ('Ingresa el importe: ')
        try:
            entero=float(entero)
            print("")
            return entero
        except ValueError:
            print("\033[1;31m"+"Error, ingrese un numero.\n"+'\033[0;m')