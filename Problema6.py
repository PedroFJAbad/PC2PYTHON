# Función para generar la serie de Fibonacci hasta un límite dado
def fibonacci_hasta_limite(limite):
    a, b = 0, 1
    while a <= limite:
        print(a, end=' ')
        a, b = b, a + b

# Llamar a la función con el límite de 50
print("Serie de Fibonacci hasta 50:")
fibonacci_hasta_limite(50)