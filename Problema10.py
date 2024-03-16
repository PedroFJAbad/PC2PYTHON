def convertir_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]
    partes = fecha.split()
    if len(partes) == 3:
        dia = partes[1].replace(",", "").zfill(2)
        mes = str(meses.index(partes[0]) + 1).zfill(2)
        anio = partes[2]
    else:
        partes_fecha = fecha.split("/")
        mes = partes_fecha[0].zfill(2)
        dia = partes_fecha[1].zfill(2)
        anio = partes_fecha[2]
    return f"{anio}-{mes}-{dia}"

# Solicitar al usuario que ingrese una fecha
fecha = input("Ingresa una fecha (en formato mes-día-año o 'Mes dia, año'): ")
fecha_convertida = convertir_fecha(fecha)
print(f"La fecha en formato AAAA-MM-DD es: {fecha_convertida}")