class Biblioteca:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.libros = []
        self.usuarios = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro(self, criterio):
        # Implementación de la búsqueda, por ejemplo, por título o autor
        resultados = []
        for libro in self.libros:
            if criterio.lower() in libro.titulo.lower() or criterio.lower() in libro.autor.lower():
                resultados.append(libro)
        return resultados