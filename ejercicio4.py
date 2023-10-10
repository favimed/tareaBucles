numero = int(input("Escribe un número entero positivo: "))

if numero < 0:
    print("El número tiene que ser positivo.")
else:
    contador = numero
    cuentaAtras = ""

    while contador >= 0:
        cuentaAtras += str(contador)
        if contador > 0:
            cuentaAtras += ", "
        contador -= 1  

    print("Cuenta atrás:", cuentaAtras)