contrasena = "Hola12345"

while True:
    contrasena_ingresada = input("Contraseña: ")

    if contrasena_ingresada == contrasena:
        print("La contraseña es correcta. ¡Bienvenido!")
        break
    else:
        print("La contraseña es incorrecta")