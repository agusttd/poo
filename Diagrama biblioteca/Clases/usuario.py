import datetime

class Usuario:
    def __init__(self, nombre, direccion, habilitado, telefono, correo):
        self.nombre = nombre
        self.direccion = direccion
        self.habilitado = habilitado
        self.telefono = telefono
        self.correo = correo
        self.prestamos = []

    def solicitar_prestamo(self, libro, biblioteca):
        if libro.disponible:
            nuevo_prestamo = Prestamo(libro, self, datetime.now(), datetime.now() + timedelta(days=14))
            self.prestamos.append(nuevo_prestamo)
            libro.disponible = False
            biblioteca.prestamos.append(nuevo_prestamo)
        else:
            print("El libro no está disponible.")