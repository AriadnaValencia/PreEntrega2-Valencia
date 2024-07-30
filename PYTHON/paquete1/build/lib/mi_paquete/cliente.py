class Cliente:
    def __init__(self, nombre, email, telefono, direccion):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.direccion = direccion

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email
        print(f"Email actualizado a {self.email}")

    def actualizar_telefono(self, nuevo_telefono):
        self.telefono = nuevo_telefono
        print(f"Teléfono actualizado a {self.telefono}")

    def __str__(self):
        return f"Cliente: {self.nombre}, Email: {self.email}, Teléfono: {self.telefono}, Dirección: {self.direccion}"
