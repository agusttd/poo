import re

class Libro:
    def __init__(self, isbn, titulo, autor, genero, formato, num_paginas, editorial, año):
        self.isbn = self._validar_isbn(isbn)
        self.titulo = titulo  #Validar que no este vacio
        self.autor = autor  #Validar que no este vacio
        self.genero = genero
        self.formato = formato
        self.num_paginas = num_paginas
        self.editorial = editorial
        self.año = año  #Validar que sea un año valido (no uno negativo)
        self.disponible = True  #Inicialmente, el libro esta disponible

    def _validar_isbn(self, isbn): #Validacion del ISBN, por ejemplo, utilizando una expresión regular
        if not re.match(r"^\d{13}$", isbn):
            raise ValueError("ISBN inválido. Debe tener 13 dígitos.")
        return isbn

    def __str__(self):
        return f"Libro: {self.titulo} ({self.autor})"

    def prestar(self):
        if self.disponible:
            self.disponible = False
        else:
            print("El libro ya está prestado.")

    def devolver(self):
        self.disponible = True