# Clase base o principal que guarda los datos generales de un empleado
class employee: 
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}")

# Clase hija (manager) que hereda de employee y le agrega el departamento
class manager(employee):
    def __init__(self, name, salary, department):
        #el super() llama al constructor de la clase padre (employee) para inicializar name y salary
        super().__init__(name, salary)
        self.department = department

    # Sobrescribimos el método show_info para que ahora muestre también el departamento
    def show_info(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Department: {self.department}")

# Creamos un objeto de tipo manager y mostramos su información completa
employee1 = employee("Alice", 40000)
manager1 = manager("Laura", 60000, "Networking")
employee1.show_info()    
manager1.show_info()