def contar_digitos(numero, digito):
    return str(numero).count(str(digito))

# Solicitar al usuario que ingrese el número y el dígito
try:
    numero = int(input("Ingresa un número entero: "))
    digito = int(input("Ingresa un dígito: "))
    cantidad = contar_digitos(numero, digito)
    print(f"El dígito {digito} aparece {cantidad} veces en el número {numero}.")
except ValueError:
    print("Por favor, ingresa un número entero válido.")