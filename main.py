from base_de_datos import BaseDatos
from producto_dao import ProductoDAO
from producto_servicio import ProductoServicio

def solicitar_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print(" Error: Debe ingresar un número entero válido.")

def solicitar_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print(" Error: Debe ingresar un valor numérico válido.")

def main():
    db = BaseDatos()
    db.inicializar_base_datos()
    
    dao = ProductoDAO(db)
    servicio = ProductoServicio(dao)

    while True:
        print("\n========================================")
        print("    SISTEMA DE INVENTARIO DE VIDEOJUEGOS")
        print("========================================")
        print("1. Registrar videojuego")
        print("2. Mostrar inventario")
        print("3. Buscar videojuego por ID")
        print("4. Actualizar videojuego")
        print("5. Eliminar videojuego")
        print("6. Vender unidades")
        print("7. Salir")
        print("========================================")
        
        opcion = solicitar_entero("Seleccione una opción (1-7): ")

        if opcion == 1:
            print("\n--- Registrar Videojuego ---")
            nombre = input("Ingrese el nombre del videojuego: ")
            precio = solicitar_flotante("Ingrese el precio: ")
            stock = solicitar_entero("Ingrese la cantidad disponible (stock): ")
            
            exito, mensaje = servicio.registrar_producto(nombre, precio, stock)
            print(f"{' if exito else '} {mensaje}")

        elif opcion == 2:
            print("\n--- Inventario de Videojuegos ---")
            productos = servicio.listar_productos()
            if not productos:
                print(" El inventario está vacío.")
            else:
                for p in productos:
                    print(p)

        elif opcion == 3:
            print("\n--- Buscar Videojuego ---")
            id_prod = solicitar_entero("Ingrese el ID del videojuego a buscar: ")
            producto, mensaje = servicio.buscar_producto(id_prod)
            if producto:
                print(f" {mensaje}")
                print(producto)
            else:
                print(f" {mensaje}")

        elif opcion == 4:
            print("\n--- Actualizar Videojuego ---")
            id_prod = solicitar_entero("Ingrese el ID del videojuego a actualizar: ")
            producto_antiguo, msg = servicio.buscar_producto(id_prod)
            
            if not producto_antiguo:
                print(f" {msg}")
            else:
                print(f"Información actual: {producto_antiguo}")
                nombre = input("Ingrese el nuevo nombre: ")
                precio = solicitar_flotante("Ingrese el nuevo precio: ")
                stock = solicitar_entero("Ingrese el nuevo stock: ")
                
                exito, mensaje = servicio.actualizar_producto(id_prod, nombre, precio, stock)
                print(f"{' if exito else '} {mensaje}")

        elif opcion == 5:
            print("\n--- Eliminar Videojuego ---")
            id_prod = solicitar_entero("Ingrese el ID del videojuego a eliminar: ")
            exito, mensaje = servicio.eliminar_producto(id_prod)
            print(f"{' if exito else '} {mensaje}")

        elif opcion == 6:
            print("\n--- Venta de Videojuegos ---")
            id_prod = solicitar_entero("Ingrese el ID del videojuego a vender: ")
            cantidad = solicitar_entero("Ingrese la cantidad que desea vender: ")
            
            exito, mensaje = servicio.vender_unidades(id_prod, cantidad)
            print(f"{' if exito else '} {mensaje}")

        elif opcion == 7:
            print("\n¡Gracias por utilizar el Sistema de Inventario! Saliendo...")
            break
        else:
            print(" Opción inválida. Por favor, elija un número entre 1 y 7.")

if __name__ == "__main__":
    main()