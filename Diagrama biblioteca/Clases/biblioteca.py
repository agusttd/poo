import prestamo
import usuario
import libro

class Biblioteca:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.libros = []
        self.usuarios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, criterio):     #Implementación de la busqueda, ej: por título o autor
        resultados = []
        for libro in self.libros:
            if criterio.lower() in libro.titulo.lower() or criterio.lower() in libro.autor.lower():
                resultados.append(libro)
        return resultados

    def prestar_libro(self, usuario_id, libro_id):
        usuario = self.buscar_usuario(usuario_id)
        libro = self.buscar_libro(libro_id)
        if usuario and libro:
            usuario.solicitar_prestamo(libro, self)
        else:
            print("Usuario o libro no encontrado.")

    def eliminar_libro(self, libro): 
        for prestamo in self.prestamos:
            if prestamo.libro == libro:
                print("No se puede eliminar el libro. Está prestado.") #Verifica si el libro esta prestado antes de eliminarlo
                return
            self.libros.remove(libro)