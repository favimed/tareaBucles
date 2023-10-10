numero = int(input("Escribe un número entero positivo: "))

if numero <= 0:
    print("El número tiene que ser positivo.")
else:
    impares = []

    for i in range(1, numero + 1):
        if i % 2 == 1:
            impares.append(str(i))
    numeros_impares = ', '.join(impares)

    print("Los numeros impares desde 1 hasta", numero, "son :", numeros_impares)