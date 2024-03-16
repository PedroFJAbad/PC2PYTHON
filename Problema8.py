def factorial(numero):
    if numero < 0:
        return "El factorial no está definido para números negativos."
    elif numero == 0:
        return 1
    else:
        fact = 1
        for i in range(1, numero + 1):
            fact *= i
        return fact

# Solicitar al usuario que ingrese un número
try:
    num = int(input("Ingresa un número entero no negativo: "))
    print(f"El factorial de {num} es: {factorial(num)}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")