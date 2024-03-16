def omitir_vocales(cadena):
    vocales = "aeiouAEIOU"
    cadena_sin_vocales = ""
    for letra in cadena:
        if letra not in vocales:
            cadena_sin_vocales += letra
    return cadena_sin_vocales

# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingresa una cadena de texto: ")
cadena_sin_vocales = omitir_vocales(cadena)
print("Cadena sin vocales:", cadena_sin_vocales)