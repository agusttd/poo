class Prestamo:
    def __init__(self, libro, usuario, fecha_prestamo, fecha_devolucion_prevista):
        self.libro = libro
        self.usuario = usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion_prevista = fecha_devolucion_prevista
        self.estado = "En curso"
