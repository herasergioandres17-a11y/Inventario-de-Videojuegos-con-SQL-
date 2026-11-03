from modelo import Producto
import sqlite3


class ProductoDAO:
    def __init__(self, base_datos):
        self.base_datos = base_datos

    def insertar(self, producto: Producto):
        conexion = self.base_datos.conectar()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO videojuegos (nombre, precio, stock) VALUES (?, ?, ?)",
                (producto.nombre, producto.precio, producto.stock),
            )
            conexion.commit()
            producto.id_producto = cursor.lastrowid
            return True
        except sqlite3.Error as e:
            print(f"Error al insertar el producto: {e}")
            return False
        finally:
            conexion.close()

    def obtener_todos(self):
        productos = []
        conexion = self.base_datos.conectar()
        if not conexion:
            return productos
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, precio, stock FROM videojuegos")
            for fila in cursor.fetchall():
                productos.append(Producto(fila[0], fila[1], fila[2], fila[3]))
        except sqlite3.Error as e:
            print(f"Error al obtener los productos: {e}")
        finally:
            conexion.close()
        return productos

    def obtener_por_id(self, id_producto):
        conexion = self.base_datos.conectar()
        if not conexion:
            return None
        producto = None
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id, nombre, precio, stock FROM videojuegos WHERE id = ?",
                (id_producto,),
            )
            fila = cursor.fetchone()
            if fila:
                producto = Producto(fila[0], fila[1], fila[2], fila[3])
        except sqlite3.Error as e:
            print(f"Error al buscar el producto: {e}")
        finally:
            conexion.close()
        return producto

    def actualizar(self, producto: Producto):
        conexion = self.base_datos.conectar()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE videojuegos SET nombre = ?, precio = ?, stock = ? WHERE id = ?",
                (producto.nombre, producto.precio, producto.stock, producto.id_producto),
            )
            conexion.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error al actualizar el producto: {e}")
            return False
        finally:
            conexion.close()

    def eliminar(self, id_producto):
        conexion = self.base_datos.conectar()
        if not conexion:
            return False
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM videojuegos WHERE id = ?", (id_producto,))
            conexion.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error al eliminar el producto: {e}")
            return False
        finally:
            conexion.close()
                                           
                                        
                                
                                