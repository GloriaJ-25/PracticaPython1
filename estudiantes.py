def ingresar_datos():
    estudiantes = {}
    cantidad = int(input("¿Cuántos estudiantes vas a ingresar? "))
    for i in range(cantidad):
        nombre = input(f"Nombre del estudiante {i+1}: ")
        notas = input("Ingresa las calificaciones separadas por comas: ")
        calificaciones = [float(n) for n in notas.split(",")]
        estudiantes[nombre] = calificaciones
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {}
    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        promedios[nombre] = promedio
    return promedios

def mejor_estudiante(promedios):
    return max(promedios, key=promedios.get)

def guardar_resultados(estudiantes, promedios, mejor):
    with open("resultados.txt", "w") as archivo:
        for nombre in estudiantes:
            archivo.write(f"{nombre}: {estudiantes[nombre]} -> Promedio: {promedios[nombre]:.2f}\n")
        archivo.write(f"\nEl mejor estudiante es: {mejor} con promedio {promedios[mejor]:.2f}\n")

def main():
    estudiantes = ingresar_datos()
    promedios = calcular_promedios(estudiantes)
    mejor = mejor_estudiante(promedios)
    guardar_resultados(estudiantes, promedios, mejor)
    print("¡Resultados guardados en resultados.txt!")

if __name__ == "__main__":
    main()
