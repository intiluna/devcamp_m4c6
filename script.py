class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

    def __str__(self):
        return(f"Usuario con nombre: {self.nombre} y contraseña (no compartir): {self.contrasena}")

user1 = Usuario("Ernesto", "LaClave+dificil4754673")

print(user1)
print(type(user1))