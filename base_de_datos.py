import sqlite3

class BaseDatos:
    def __init__(self, nombre_bd="inventario_videojuegos.db"):
        self.nombre_bd = nombre_bd

    def conectar(self):
        try:
            conexion = sqlite3.connect(self.nombre_bd)
            return conexion
        except sqlite3.Error as e:
            print(f"Error al conectar con la base de datos: {e}")
            return None

    def inicializar_base_datos(self):
        conexion = self.conectar()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS videojuegos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        precio REAL NOT NULL,
                        stock INTEGER NOT NULL
                    )
                """)
                conexion.commit()
            except sqlite3.Error as e:
                print(f"Error al iniciar la tabla: {e}")
            finally:
                conexion.close()