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
        opcionMmF=fn.menu_mod_fac()
        if opcionMmF == 1:
            fn.Modificar_fac_cuil()
        elif opcionMmF == 2:
            fn.Modificar_fac_dir()
        elif opcionMmF == 3:
            fn.Modificar_fac_dia()
        elif opcionMmF == 4:
            fn.Modificar_fac_mes()
        elif opcionMmF == 5:
            fn.Modificar_fac_año()
        elif opcionMmF == 6:
            fn.Modificar_fac_importe()
        elif opcionMmF == 7:
            fn.Modificar_fac_descripcion()
        elif opcionMmF == 8:
            os.system('cls')
            continue
    elif opcion==4:
        fn.Eliminar_fac()
    elif opcion==5:
        break