class Producto:
    def __init__(self, id_producto=None, nombre="", precio=0.0, stock=0):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Precio: ${self.precio:,.2f} | Stock: {self.stock} unidades"