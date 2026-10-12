# Primera clase con su respectiva función para generar reportes
class accountant:
    def generate_report(self):
        print("Generating financial report")

# Segunda clase con su funcion para reparar maquinas
class technician:
    def repair_machine(self):
        print("Repairing machine")

# Clase jefe que hace herencia multiple: junta las habilidades de contador y técnico
class boss(accountant, technician):
    pass

# Creamos al jefe y probamos que puede hacer ambas acciones sin problema
boss1 = boss()
boss1.generate_report()
boss1.repair_machine()