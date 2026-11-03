from modelo import Producto
from producto_dao import ProductoDAO

class ProductoServicio:
    def __init__(self, producto_dao: ProductoDAO):
        self.producto_dao = producto_dao

    def registrar_producto(self, nombre, precio, stock):
        nombre = nombre.strip()
        if not nombre:
            return False, "El nombre del videojuego no puede estar vacío."
        if precio <= 0:
            return False, "El precio debe ser mayor a cero."
        if stock < 0:
            return False, "El stock no puede ser negativo."

        nuevo_producto = Producto(nombre=nombre, precio=precio, stock=stock)
        exito = self.producto_dao.insertar(nuevo_producto)
        if exito:
            return True, "Producto guardado correctamente."
        return False, "Error en la base de datos al guardar el producto."

    def listar_productos(self):
        return self.producto_dao.obtener_todos()

    def buscar_producto(self, id_producto):
        producto = self.producto_dao.obtener_por_id(id_producto)
        if not producto:
            return None, f"El videojuego con ID {id_producto} no existe."
        return producto, "Producto encontrado con éxito."

    def actualizar_producto(self, id_producto, nombre, precio, stock):
        producto_existente = self.producto_dao.obtener_por_id(id_producto)
        if not producto_existente:
            return False, f"No se puede actualizar. El ID {id_producto} no existe."

        nombre = nombre.strip()
        if not nombre:
            return False, "El nombre no puede estar vacío."
        if precio <= 0:
            return False, "El precio debe ser mayor a cero."
        if stock < 0:
            return False, "El stock no puede ser negativo."

        producto_existente.nombre = nombre
        producto_existente.precio = precio
        producto_existente.stock = stock

        exito = self.producto_dao.actualizar(producto_existente)
        if exito:
            return True, "Producto actualizado correctamente."
        return False, "No se pudo actualizar el producto."

    def eliminar_producto(self, id_producto):
        producto_existente = self.producto_dao.obtener_por_id(id_producto)
        if not producto_existente:
            return False, f"No se puede eliminar. El ID {id_producto} no existe."

        exito = self.producto_dao.eliminar(id_producto)
        if exito:
            return True, "El producto ha sido eliminado del inventario."
        return False, "Error al intentar eliminar el producto."

    def vender_unidades(self, id_producto, cantidad):
        if cantidad <= 0:
            return False, "La cantidad a vender debe ser mayor a cero."

        producto = self.producto_dao.obtener_por_id(id_producto)
        if not producto:
            return False, f"El videojuego con ID {id_producto} no existe."

        if producto.stock < cantidad:
            return False, f"Operación rechazada. Stock insuficiente (Disponible: {producto.stock}, Solicitado: {cantidad})."

        producto.stock -= cantidad
        exito = self.producto_dao.actualizar(producto)
        if exito:
            return True, f"Venta realizada con éxito. Nuevo stock: {producto.stock}."
        return False, "Error al procesar la venta."