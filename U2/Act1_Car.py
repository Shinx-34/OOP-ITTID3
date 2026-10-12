#clase base Car
class Car:
    #Se definen las partes del carro siendo estas la marca, el modelo y el color. 
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    #se define lo que se imprimira.
    def show_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Color: {self.color}")

#se establecen las partes "self" del anterior segmento 
car1 = Car("Chevrolet", "Suburban", "Blanco")
car2 = Car("Toyota", "Tacoma", "Azul")

#se muestra la infomacion ya unida en su totalidad 
car1.show_info()
car2.show_info()