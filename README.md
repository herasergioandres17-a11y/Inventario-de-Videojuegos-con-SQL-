# Sistema de Inventario de Videojuegos (Patrón DAO + SQLite)

## Propósito del Proyecto
Aplicación desarrollada en Python bajo una arquitectura por capas (Modelo, Base de Datos, DAO, Servicio y Vista) que permite administrar de forma persistente el inventario de una tienda de videojuegos utilizando SQLite.

## Estructura del Proyecto
- `modelo.py`: Contiene la clase `Producto` que modela la entidad principal.
- `base_datos.py`: Administra la conexión nativa con SQLite y la creación automática de la tabla.
- `producto_dao.py`: Encapsula todas las sentencias SQL (CRUD) aislando la lógica de persistencia.
- `producto_servicio.py`: Contiene las reglas de negocio, validaciones estrictas y control de errores.
- `main.py`: Interfaz de usuario por consola con menú interactivo y control de excepciones por entradas incorrectas.

## Instrucciones de Ejecución
1. Asegúrate de tener instalado **Python 3.x**.
2. Clona este repositorio o descarga los archivos en una misma carpeta.
3. Ejecuta el programa principal desde tu terminal o IDE preferido (como VS Code):
   ```bash
   python main.py