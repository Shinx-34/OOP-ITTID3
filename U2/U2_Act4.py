# Clase Motor con su accion basica de arrancar
class Motor:
    def arrancar(self):
        print("Motor encendido")

# Clase Auto que por dentro lleva un motor asignado 
class Auto:
    def __init__(self, motor):
        self.motor = motor

    # Método para encender el carro usando la accion del motor interno
    def arrancar_auto(self):
        self.motor.arrancar()

# Creamos primero el motor, luego se lo metemos al auto y lo encendemos
motor = Motor()
auto1 = Auto(motor)
auto1.arrancar_auto()