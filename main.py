from tarea import Tarea
from gestor import GestorTareas

def mostrar_menu():
    print("\n📝 Gestor de Tareas")
    print("1. Agregar tarea")
    print("2. Mostrar tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    gestor = GestorTareas()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre de la tarea: ")
            descripcion = input("Descripción: ")
            tarea = Tarea(nombre, descripcion)
            gestor.agregar_tarea(tarea)
            
        elif opcion == "2":
            gestor.mostrar_tareas()
            
        elif opcion == "3":
            nombre = input("Nombre de la tarea a completar: ")
            gestor.marcar_completada(nombre)
            
        elif opcion == "4":
            nombre = input("Nombre de la tarea a eliminar: ")
            gestor.eliminar_tarea(nombre)
            
        elif opcion == "5":
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()