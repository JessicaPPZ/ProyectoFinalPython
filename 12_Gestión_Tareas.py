class Producto:
    def __init__(self, titulo, descripcion, estado):
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = estado
def mostrar_menu():
    print("Sistema de Gestión de Tareas")
    print("1. agregar nueva tarea")
    print("2. mostrar tareas")
    print("3. buscar tarea")
    print("4. actualizar tarea")
    print("5. eliminar tarea")
    print("6. salir")
inventario = []
while True:
    mostrar_menu()
    opcion = input("elige una opcion: ")
    if opcion == "6":
        print("saliendo del programa")
        break
    if opcion == "1":        
        try:
            titulo = input("ingresa el titulo de la tarea: ")
            descripcion = input("ingresa la descripcion: ")
            estado = input("ingresa el estado: ")
            producto = Producto(titulo, descripcion, estado)
            inventario.append(producto)
            print("tarea agregada")
        except ValueError:
            print("error: entrada no valida")
    elif opcion == "2":
        if inventario:
            for p in inventario:
                print(f"titulo: {p.titulo}, descripcion: {p.descripcion}, estado: {p.estado}")
        else:
            print("no hay tarea en el inventario")
    elif opcion == "3":
        titulo = input("ingresa el titulo de la tarea a buscar: ")
        encontrado = False
        for p in inventario:
            if p.titulo == titulo:
                print(f"titulo: {p.titulo}, descripcion: {p.descripcion}, estado: {p.estado}")
                encontrado = True
                break
        if not encontrado:
            print("tarea no encontrada")
    elif opcion == "4":
        titulo = input("ingresa el titulo de la tarea a actualizar: ")
        try:
            nueva_estado = input("ingresa el nuevo estado: ")
            encontrado = False
            for p in inventario:
                if p.titulo == titulo:
                    p.estado = nueva_estado
                    print("estado actualizado")
                    encontrado = True
                    break
        except ValueError:
            print("eror: entrada no valida")
    elif opcion == "5":
        titulo = input("ingresa el titulo de la tarea a eliminar: ")
        for p in inventario:
            if p.titulo == titulo:
                inventario.remove(p)
                print("tarea eliminada")
                break
    else:
        print("opcion no valida. intentalo de nuevo")