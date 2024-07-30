# Diccionario para almacenar la información de los usuarios
usuarios = {}

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre_usuario = input("Introduce tu nombre de usuario: ")
    if nombre_usuario in usuarios:
        print("Este nombre de usuario ya existe. Por favor, elige otro.")
    else:
        contraseña = input("Introduce tu contraseña: ")
        usuarios[nombre_usuario] = contraseña
        print(f"Usuario {nombre_usuario} registrado con éxito.")

# Función para verificar el login de un usuario
def login_usuario():
    nombre_usuario = input("Introduce tu nombre de usuario: ")
    contraseña = input("Introduce tu contraseña: ")
    if nombre_usuario in usuarios and usuarios[nombre_usuario] == contraseña:
        print("Login exitoso.")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

# Función para mostrar todos los usuarios registrados
def mostrar_usuarios():
    if usuarios:
        print("Usuarios registrados:")
        for usuario, contraseña in usuarios.items():
            print(f"Usuario: {usuario}, Contraseña: {contraseña}")
    else:
        print("No hay usuarios registrados.")

# Menú principal
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar usuario")
        print("2. Mostrar usuarios")
        print("3. Login")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            mostrar_usuarios()
        elif opcion == "3":
            login_usuario()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Ejecutar el menú principal
menu()
