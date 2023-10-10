cantidadInvertida = float(input("¿Que cantidad que quiere invertir?: "))
tasaInteresAnual = float(input("Ingrese la tasa de interés anual (%): "))
numeroAnios = int(input("Ingrese el número de años: "))

tasaInteresAnual /= 100

for anio in range(1, numeroAnios + 1):
    capitalObtenido = cantidadInvertida * (1 + tasaInteresAnual) ** anio
    print("Año", anio, ":", capitalObtenido, "euros")


capitalTotal = cantidadInvertida * (1 + tasaInteresAnual) ** numeroAnios
print("Capital total al final de", numeroAnios, "años:", capitalTotal, "euros")