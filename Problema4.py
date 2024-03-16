# Lista para almacenar los datos de los alumnos
alumnos = []

# Solicitar al usuario la cantidad de alumnos
num_alumnos = int(input("Ingrese la cantidad de alumnos: "))

# Iterar sobre la cantidad de alumnos para ingresar sus datos
for i in range(num_alumnos):
    nombre = input("Ingrese el nombre del alumno: ")
    calificaciones = []
    for j in range(3):
        calificacion = int(input(f"Ingrese la calificación {j+1} del alumno {nombre}: "))
        calificaciones.append(calificacion)
    
    # Agregar los datos del alumno a la lista como un diccionario
    alumnos.append({"Alumno": nombre, "Notas": calificaciones})

# Mostrar el listado completo de alumnos
print("\nListado de alumnos:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Notas: {alumno['Notas']}")