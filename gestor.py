class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def eliminar_tarea(self, nombre_tarea):
        for tarea in self.tareas:
            if tarea.nombre == nombre_tarea:
                self.tareas.remove(tarea)
                return True
        return False

    def mostrar_tareas(self):
        for tarea in self.tareas:
            estado = "✓" if tarea.completada else "✗"
            print(f"{tarea.nombre} - {estado}")