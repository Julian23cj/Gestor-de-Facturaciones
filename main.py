import funciones as fn
import base_de_datos as bd
import os

con, cur= bd.conectar()
bd.crear_tabla(con, cur)

fn.crear_base_datos()

while True:
    opcion = fn.menu_principal()

    if opcion==1:
        opcionMf=fn.menu_buscar_facturaciones()
        if opcionMf==1:
            fn.todas_facturaciones()
        elif opcionMf==2:
            fn.ultimas_dies_facturaciones()
        elif opcionMf==3:
            fn.buscar_fac_fecha_mes()
        elif opcionMf==4:
            fn.buscar_fac_cuil()
        elif opcionMf==5:
            fn.buscar_fac_direccion()
        elif opcionMf==6:
            os.system('cls')
            continue
    elif opcion==2:
        bd.insertar_datos()
    elif opcion==3:
        print("en desarrollo 3")
    elif opcion==4:
        print("en desarrollo 4")
    elif opcion==5:
        print("en desarrollo 5")
        break
    