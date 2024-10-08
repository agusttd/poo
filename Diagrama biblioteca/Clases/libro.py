import re

class Libro:
    def __init__(self, isbn, titulo, autor, genero, formato, num_paginas, editorial, año, disponible=True):
        self.isbn = self._validar_isbn(isbn)
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.formato = formato
        self.num_paginas = num_paginas
        self.editorial = editorial
        self.año = año
        self.disponible = disponible

    def _validar_isbn(self, isbn):
        # Validación del ISBN, por ejemplo, utilizando una expresión regular
        if not re.match(r"^\d{13}$", isbn):
            raise ValueError("ISBN inválido. Debe tener 13 dígitos.")
        return isbn

    # ... Otros métodos de validación para los demás atributos

    def __str__(self):
        return f"Libro: {self.titulo} ({self.autor})"