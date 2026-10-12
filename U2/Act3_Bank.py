class BankAccount:
    # Aqui definimos un dato general que aplica para todas las cuentas por igual
    bank = "Central Bank"

    # El constructor donde guardamos el nombre del cliente y su dinero en dolares
    def __init__(self, client, balance):
        self.client = client
        self.balance = balance  # en dolares

    # Esta funcion (metodo) sirve para ver los datos particulares de cada cuenta
    def show_balance(self):
        print(f"Customer: {self.client} - balance: ${self.balance} USD")

    # Esta funcion usa el decorador para mostrar el nombre del banco global
    @classmethod
    def show_bank(cls):
        print(f"Bank: {cls.bank}")

    # Esta es una funcion independiente (estática) que solo hace un calculo rapido de dinero
    @staticmethod
    def convert_currency(value):
        # Aplicamos un tipo de cambio fijo de ejemplo
        pesos = value * 17.50
        print(f"${value} USD = ${pesos} MXN")
        return pesos

# Creamos la primera cuenta con su cliente y saldo
cuenta1 = BankAccount("Juan", 500)

cuenta1.show_balance() # Mandamos a llamar el saldo de la cuenta
BankAccount.show_bank() # Mostramos el banco general desde la clase
BankAccount.convert_currency(100)  # Convertimos dolares a pesos con el metodo estatico
cuenta1.show_bank()