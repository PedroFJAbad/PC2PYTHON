# Número de filas del patrón
filas = 5

# Imprimir la parte superior del patrón
for x in range(filas):
    for y in range(x + 1):
        print("*", end=" ")
    print()

# Imprimir la parte inferior del patrón
for x in range(filas - 1, 0, -1):
    for y in range(x):
        print("*", end=" ")
    print()