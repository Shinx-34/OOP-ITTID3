#se define la clase persona
class Person:
    #se definen las partes de la clase persona.
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    #se define el saludo de la persona.
    def greet(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and I live in {self.city}.")

#Se establecen los datos que entregara la persona tal cual.
person1 = Person("Juan", 15, "Guadalajara")
person2 = Person("Maria", 22, "Tijuana")
person3 = Person("Mateo", 18, "Culiacan")
person4 = Person(15, "Upen", "Alice")

#se muestra la informacion ya unida
person1.greet()
person2.greet()
person3.greet()
person4.greet()