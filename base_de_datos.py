import sqlite3
import funciones as fn

def conectar():
    conexion= sqlite3.connect("Facturaciones.db")
    cursor=conexion.cursor()
    return conexion, cursor

def crear_tabla(conexion,cursor):
    sentencia="""
        CREATE TABLE IF NOT EXISTS Facturaciones
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        N°FACTURACION INT NOT NULL,
        CUIL INT NOT NULL,
        DIRECCION TEXT NOT NULL,
        DÍA INT NOT NULL,
        MES INT NOT NULL,
        AÑO INT NOT NULL,
        IMPORTE REAL NOT NULL,
        DESCRIPCION TEXT);
    """
    cursor.execute(sentencia)
    conexion.close()
    #print("Tabla creada correctamente.")

def insertar_datos():
    numeroFac, cuil, direccion, dia, mes, anio, importe, descripcion=fn.crear_facturacion()
    conexion,cursor= conectar()
    
        
    cursor.execute('''INSERT INTO Facturaciones (N°FACTURACION, CUIL, DIRECCION, DÍA, MES, AÑO, IMPORTE, DESCRIPCION) 
    VALUES(?,?,?,?,?,?,?,?)''', (numeroFac, cuil, direccion, dia, mes, anio, importe, descripcion))
    conexion.commit()
    conexion.close()
    print("\033[1;31m"+"Facturación creada correctamente.\n"+'\033[0;m')
