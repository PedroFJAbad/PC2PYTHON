numeros = []  # Lista para almacenar los números ingresados

while True:
    respuesta = input("Desea ingresar un número? (SI/NO): ")
    if respuesta.upper() == "SI":
        numero = int(input("Ingrese el número: "))
        numeros.append(numero)
    elif respuesta.upper() == "NO":
        break
    else:
        print("Respuesta inválida. Por favor, responda SI o NO.")

# Contar la cantidad de números pares e impares
numeros_pares = len([num for num in numeros if num % 2 == 0])
numeros_impares = len([num for num in numeros if num % 2 != 0])

# Imprimir resultados
print("Números ingresados:", numeros)
print("Cantidad de números pares:", numeros_pares)
print("Cantidad de números impares:", numeros_impares)