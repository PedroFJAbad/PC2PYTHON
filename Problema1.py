# Inicializar una lista vacía para almacenar los números que cumplen las condiciones
numeros_cumplen_condiciones = []

# Iterar sobre el rango de 1500 a 2700 (ambos incluidos)
for numero in range(1500, 2700):
    # Verificar si el número es divisible por 7 y múltiplo de 5
    if numero % 7 == 0 and numero % 5 == 0:
        # Si cumple las condiciones, agregarlo a la lista
        numeros_cumplen_condiciones.append(numero)

# Imprimir los números que cumplen las condiciones
print("Los números divisibles por 7 y múltiplos de 5 en el rango de 1500 a 2700 son:")
print(numeros_cumplen_condiciones)