import os


def ingreso_por_carpeta(directorio_inicial=None):
    """Función que permite al usuario navegar por los directorios."""
    if directorio_inicial is None:
        directorio_inicial = os.getcwd()  # Usar el directorio de trabajo actual si no se proporciona uno

    directorio_actual = directorio_inicial

    while True:
        print(f"Directorio actual: {directorio_actual}")
        archivos = os.listdir(directorio_actual)
        for idx, archivo in enumerate(archivos):
            print(f"{idx}: {archivo}")

        seleccion = input(
            'Ingresa el número de la carpeta a la que quieras acceder, "volver" para subir un nivel, "salir" para terminar o "cambiar" para ingresar un nuevo directorio inicial: ')

        if seleccion.lower() == 'salir':
            break  # Salir de la función
        elif seleccion.lower() == 'volver':
            directorio_actual = os.path.dirname(directorio_actual)  # Subir un nivel en la jerarquía de directorios
        elif seleccion.lower() == 'cambiar':
            nuevo_directorio = input('Ingresa el nuevo directorio inicial: ')
            if os.path.isdir(nuevo_directorio):
                directorio_actual = nuevo_directorio
            else:
                print("El directorio ingresado no es válido.")
        elif seleccion.isdigit() and int(seleccion) in range(len(archivos)):
            seleccion = int(seleccion)
            ruta_seleccionada = os.path.join(directorio_actual, archivos[seleccion])
            if os.path.isdir(ruta_seleccionada):
                directorio_actual = ruta_seleccionada  # Cambiar a la carpeta seleccionada
            else:
                print(f"'{archivos[seleccion]}' no es una carpeta. Por favor, selecciona una carpeta.")
        else:
            print("Selección no válida. Intenta de nuevo.")


# Llamar a la función sin parámetros iniciará en el directorio actual del usuario
ingreso_por_carpeta()
