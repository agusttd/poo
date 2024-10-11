import biblioteca
import datetime
import prestamo

class Usuario:
    def __init__(self, nombre, direccion, habilitado, telefono, correo):
        self.nombre = nombre
        self.direccion = direccion
        self.habilitado = habilitado  # True si el usuario está habilitado, False si está bloqueado
        self.telefono = telefono
        self.correo = correo
        self.prestamos = []
        self.limite_prestamos = 5  # Límite máximo de préstamos simultáneos

    def solicitar_prestamo(self, libro, biblioteca, fecha_devolucion=None):
        if self.habilitado and len(self.prestamos) < self.limite_prestamos:
            if libro.disponible:
                if not fecha_devolucion:
                    fecha_devolucion = datetime.datetime.now() + datetime.timedelta(days=14)
                nuevo_prestamo = prestamo(libro, self, datetime.datetime.now(), fecha_devolucion)
                self.prestamos.append(nuevo_prestamo)
                libro.disponible = False
                biblioteca.prestamos.append(nuevo_prestamo)
            else:
                print("El libro no está disponible.")
        else:
            print("El usuario no está habilitado o ha alcanzado el límite de préstamos.")

    def buscar_libro(self, criterio):  # Busca un libro en los prestamos del usuario
        resultados = []
        for prestamo in self.prestamos:
            if criterio.lower() in prestamo.libro.titulo.lower() or criterio.lower() in prestamo.libro.autor.lower():
                resultados.append(prestamo.libro)
        return resultados
