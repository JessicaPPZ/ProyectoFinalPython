class Producto:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
def mostrar_menu():
    print("sistema de inventario")
    print("1. agregar producto")
    print("2. mostrar productos")
    print("3. buscar producto")
    print("4. actualizar cantidad")
    print("5. eliminar producto")
    print("6. salir")
inventario = []
while True:
    mostrar_menu()
    opcion = input("elige una opcion: ")
    if opcion == "6":
        print("saliendo del programa")
        break
    if opcion == "1":
        nombre = input("ingresa el nombre del producto: ")
        try:
            cantidad = int(input("ingresa la cantidad: "))
            precio = float(input("ingresa el precio: "))
            producto = Producto(nombre, cantidad, precio)
            inventario.append(producto)
            print("tarea agregada")
        except ValueError:
            print("error: entrada no valida")
    elif opcion == "2":
        for p in inventario:
            print(f"nombre: {p.nombre}, cantidad: {p.cantidad}, precio: {p.precio}")
    elif opcion == "3":
        nombre = input("ingresa el nombre del producto a buscar: ")
        encontrado = False
        for p in inventario:
            if p.nombre == nombre:
                print(f"nombre: {p.nombre}, cantidad: {p.cantidad}, precio: {p.precio}")
                encontrado = True
                break
        if not encontrado:
            print("producto no encontrado")
    elif opcion == "4":
        nombre = input("ingresa el nombre del producto a actualizar: ")
        try:
            nueva_cantidad = int(input("ingresa la nueva cantidad: "))
            for p in inventario:
                if p.nombre == nombre:
                    p.cantidad = nueva_cantidad
                    print("cantidad actualizadad")
                    break
        except ValueError:
            print("eror: entrada no valida")
    elif opcion == "5":
        nombre = input("ingresa el nombre del producto a eliminar: ")
        for p in inventario:
            if p.nombre == nombre:
                inventario.remove(p)
                print("producto eliminado")
                break
    else:
        print("opcion no valida. intentalo de nuevo")