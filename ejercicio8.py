frase = input("Escribe una frase: ")
letra = input("Elige una letra: ")

letra = letra.lower()
contador = 0

for caracter in frase:
    caracter = caracter.lower()
    if caracter == letra:
        contador += 1

print("La letra", letra, "aparece", contador, "veces en la frase.")
