import sqlite3

def conectar():
    conexion= sqlite3.connect("Gestor-de-facturaciones.db")
    cursor=conexion.cursor()
    return conexion,cursor

def crear_tabla(conexion,cursor):
    sentencia="""
        CREATE TABLE IF NOT EXISTS Facturaciones
        (ID INTEGER PRIMARY KEY NOT NULL,
        N°FACTURACION INT NOT NULL,
        CUIL INT NOT NULL,
        DIRECCION TEXT NOT NULL,
        DIA INT NOT NULL,
        MES INT NOT NULL,
        AÑO INT NOT NULL,
        IMPORTE DOUBLE NOT NULL,
        DESCRIPCION TEXT);
    """
    cursor.execute(sentencia)
    conexion.close()
    print("Tabla creada correctamente.")

if __name__ == "__main__":
    con,cursor= conectar()

    crear_tabla(con,cursor)