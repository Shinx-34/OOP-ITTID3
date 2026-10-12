# Polimorfismo: Un metodo puede comportarse de diferentes maneras dependiendo del objeto que lo utilice.

# Clase para empleados de tiempo completo
class FulltimeEmployee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def payment(self):
        return f"{self.name} recibe un pago fijo de {self.salary}."

# Clase para empleados por hora
class HourlyEmployee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    
    def payment(self):
        total = self.hours_worked * self.hourly_rate
        return f"{self.name} recibe un pago por horas de {total}."

# Función que usa polimorfismo
def calculate_payment(worker):
    print(worker.payment())

# Probando con diferentes objetos
emp1 = FulltimeEmployee("Rocio", 5000)
emp2 = HourlyEmployee("Luis", 40, 100)

calculate_payment(emp1)  # Llama al método payment de FulltimeEmployee
calculate_payment(emp2)  # Llama al método payment de HourlyEmployee
