import os
import base_de_datos as bd
#Ctrl +k seguido de Ctrl+0
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

def menu_mod_fac():
    print("------Menu Modificación Facturaciones------\n"
    "1- Modificar Cuil.\n"
    "2- Modificar dirección.\n"
    "3- Modificar día.\n"
    "4- Modificar mes.\n"
    "5- Modificar año.\n"
    "6- Modificar importe.\n"
    "7- Modificar descripción.\n"
    "8- Volver.\n")
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

#Operacones de facturaciones

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

def Modificar_fac_cuil():
    while True:
        aux=input('¿Quiere proceder con la operación? (si/no)\n')
        if aux == 'si':
            break
        elif aux == 'no':
            os.system('cls')
            return True
    con,cur=bd.conectar()
    cur.execute('SELECT * FROM Facturaciones')
    
    NroFac=control_fac_repetidas()
    NuevoCuil=control_cuil()
    cur.execute('''UPDATE Facturaciones SET CUIL = ? WHERE N°FACTURACION = ?''', (NuevoCuil, NroFac))
    print("\033[1;32m" + "Cuil modificado correctamente.\n" + '\033[0m')
    con.commit()
    con.close()

def Modificar_fac_dir():
    while True:
        aux=input('¿Quiere proceder con la operación? (si/no)\n')
        if aux == 'si':
            break
        elif aux == 'no':
            os.system('cls')
            return True
    con,cur=bd.conectar()
    cur.execute('SELECT * FROM Facturaciones')
    
    NroFac=control_fac_repetidas()
    NuevaDic=input('Ingresa la nueva dirección: ')
    cur.execute('''UPDATE Facturaciones SET DIRECCION = ? WHERE N°FACTURACION = ?''', (NuevaDic, NroFac))
    print("\033[1;32m" + "Dirección modificado correctamente.\n" + '\033[0m')
    con.commit()
    con.close()

def Modificar_fac_dia():
    while True:
        aux=input('¿Quiere proceder con la operación? (si/no)\n')
        if aux == 'si':
            break
        elif aux == 'no':
            os.system('cls')
            return True
    con,cur=bd.conectar()
    cur.execute('SELECT * FROM Facturaciones')
    
    NroFac=control_fac_repetidas()
    NuevoDia=control_dia()
    cur.execute('''UPDATE Facturaciones SET DÍA = ? WHERE N°FACTURACION = ?''', (NuevoDia, NroFac))
    print("\033[1;32m" + "Día modificado correctamente.\n" + '\033[0m')
    con.commit()
    con.close()

def Modificar_fac_mes():
    while True:
        aux=input('¿Quiere proceder con la operación? (si/no)\n')
        if aux == 'si':
            break
        elif aux == 'no':
            os.system('cls')
            return True
    con,cur=bd.conectar()
    cur.execute('SELECT * FROM Facturaciones')
    
    NroFac=control_fac_repetidas()
    NuevoMes=control_mes()
    cur.execute('''UPDATE Facturaciones SET MES = ? WHERE N°FACTURACION = ?''', (NuevoMes, NroFac))
    print("\033[1;32m" + "Mes modificado correctamente.\n" + '\033[0m')
    con.commit()
    con.close()

def Modificar_fac_año():
    while True:
        aux=input('¿Quiere proceder con la operación? (si/no)\n')
        if aux == 'si':
            break
        elif aux == 'no':
            os.system('cls')
            return True
    con,cur=bd.conectar()
    cur.execute('SELECT * FROM Facturaciones')
    
    NroFac=control_fac_repetidas()
    NuevoAño=control_anio()
    cur.execute('''UPDATE Facturaciones SET AÑO = ? WHERE N°FACTURACION = ?''', (NuevoAño, NroFac))
    print("\033[1;32m" + "Año modificado correctamente.\n" + '\033[0m')
    con.commit()
    con.close()

def Modificar_fac_importe():
    while True:
        aux=input('¿Quiere proceder con la operación? (si/no)\n')
        if aux == 'si':
            break
        elif aux == 'no':
            os.system('cls')
            return True
    con,cur=bd.conectar()
    cur.execute('SELECT * FROM Facturaciones')
    
    NroFac=control_fac_repetidas()
    NuevoImp=control_importe()
    cur.execute('''UPDATE Facturaciones SET IMPORTE = ? WHERE N°FACTURACION = ?''', (NuevoImp, NroFac))
    print("\033[1;32m" + "Importe modificado correctamente.\n" + '\033[0m')
    con.commit()
    con.close()

def Modificar_fac_descripcion():
    while True:
        aux=input('¿Quiere proceder con la operación? (si/no)\n')
        if aux == 'si':
            break
        elif aux == 'no':
            os.system('cls')
            return True
    con,cur=bd.conectar()
    cur.execute('SELECT * FROM Facturaciones')
    
    NroFac=control_fac_repetidas()
    NuevaDes=input('Ingresa la nueva descripción: ')
    cur.execute('''UPDATE Facturaciones SET DESCRIPCION = ? WHERE N°FACTURACION = ?''', (NuevaDes, NroFac))
    print("\033[1;32m" + "Descripción modificado correctamente.\n" + '\033[0m')
    con.commit()
    con.close()

def Eliminar_fac():
    while True:
        aux=input('¿Quiere proceder con la operación? (si/no)\n')
        if aux == 'si':
            break
        elif aux == 'no':
            os.system('cls')
            return True
    con,cur=bd.conectar()
    cur.execute('SELECT * FROM Facturaciones')
    print('--Eliminar Facturación--')
    NroFac=control_fac_repetidas()
    
    cur.execute('''DELETE FROM Facturaciones WHERE N°FACTURACION = ?''', (NroFac,))
    print("\033[1;32m" + "Facturación eliminada correctamente.\n" + '\033[0m')
    con.commit()
    con.close()

#Control de errores inputs

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

def control_fac_repetidas():
    while True:
        NroFac= control_numero_facturacion()
        con,cur=bd.conectar()
        cur.execute('SELECT * FROM Facturaciones')
        datos=cur.fetchall()
        aux=False
        for control in datos:
            if NroFac == control[1]:
                aux=True
                print(f'Número de Facturación: {control[1]} CUIL: {control[2]} Dirección: {control[3]} Fecha: {control[4]}/{control[5]}/{control[6]} Importe: {control[7]} Descripción: {control[8]}')
                break
            else:
                aux=False

        if aux == True:
            con.close()
            return NroFac
        elif aux == False:
            print("\033[1;31m"+"Error, la facturación no existe, intentelo nuevamente.\n"+'\033[0;m')
            print("")
            continue

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