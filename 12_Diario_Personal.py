from datetime import datetime
class Producto:
    def __init__(self, titulo, descripcion, categorias, fecha_creacion, fecha_modificacion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.categorias = categorias
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion
def mostrar_menu():
    print("Diario Personal")
    print("1. agregar nueva nota")
    print("2. mostrar nota")
    print("3. buscar nota")
    print("4. actualizar nota")
    print("5. eliminar nota")
    print("6. salir")
def elegir_categoria():
    print("elegir una categoria: ")
    print("1. trabajo")
    print("2. personal")
    print("3. estudio")
    eleccion = input("ingresa el numero de la categoria (1-3): ")
    categorias_validas = {"1": "Trabajo", "2": "Personal", "3": "Estudio"}
    if eleccion in categorias_validas:
        return categorias_validas[eleccion]
    else:
        return None

inventario = []
while True:
    mostrar_menu()
    opcion = input("elige una opcion: ")
    if opcion == "6":
        print("saliendo del programa")
        break
    if opcion == "1":        
        try:
            titulo = input("ingresa el titulo de la nota: ")
            descripcion = input("ingresa la descripcion: ")
            categoria = elegir_categoria()
            if categoria:
                fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                producto = Producto(titulo, descripcion, categoria, fecha_actual, fecha_actual)
                inventario.append(producto)
                print("Nota agendada con exito")
            else:
                print("error")
        except ValueError:
            print("error: entrada no valida")
    elif opcion == "2":
        if inventario:
            for p in inventario:
                print(f"titulo: {p.titulo}, descripcion: {p.descripcion}, categorias: {p.categorias}, "
                      f"Fecha de creación: {p.fecha_creacion}, Fecha de modificación: {p.fecha_modificacion}")
        else:
            print("no hay nota en el inventario")
    elif opcion == "3":
        titulo = input("ingresa el titulo de la nota a buscar: ")
        encontrado = False
        for p in inventario:
            if p.titulo == titulo:
                print(f"titulo: {p.titulo}, descripcion: {p.descripcion}, categorias: {p.categorias}, "
                      f"Fecha de creación: {p.fecha_creacion}, Fecha de modificación: {p.fecha_modificacion}")
                encontrado = True
                break
        if not encontrado:
            print("nota no encontrada")
    elif opcion == "4":
        titulo = input("ingresa el titulo de la nota a actualizar: ")
        try:            
            encontrado = False
            for p in inventario:
                if p.titulo == titulo:
                    categoria = elegir_categoria()
                    if categoria:
                        p.categoria = categoria
                        p.fecha_modificacion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        print("Categoría actualizada con éxito")
                        encontrado = True
                        break
                    else:
                        print("Error: Debes elegir una categoría válida")
                        break
        except ValueError:
            print("eror: entrada no valida")
    elif opcion == "5":
        titulo = input("ingresa el titulo de la nota a eliminar: ")
        for p in inventario:
            if p.titulo == titulo:
                inventario.remove(p)
                print("nota eliminada")
                break
    else:
        print("opcion no valida. intentalo de nuevo")