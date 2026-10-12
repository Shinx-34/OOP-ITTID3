# Clase libro que recibe su titulo y número de paginas
class libro:
    def __init__(self, titulo, num_paginas):
        self.titulo = titulo
        self.num_paginas = num_paginas

    # Metodo magico __str__ para personalizar que se imprime al mandar a llamar el objeto
    def __str__(self):
        return f"Libro: {self.titulo}, Páginas: {self.num_paginas}"

    # Metodo magico __len__ para que la función len() devuelva el numero de paginas del libro
    #el __len__ se encarga de devolver un valor entero que representa la longitud del objeto, en este caso el número de páginas del libro.
    def __len__(self):
        return self.num_paginas

# Creamos el libro y probamos la impresión y el uso de len()
libro1 = libro("Cien años de soledad", 471)
print(libro1)
print("Número de páginas:", len(libro1))