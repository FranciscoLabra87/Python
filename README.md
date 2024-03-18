ingreso_por_carpeta

permite a un usuario navegar interactivamente a través del sistema de archivos utilizando la consola. Aquí te detallo su funcionamiento paso a paso:

La función acepta un argumento opcional directorio_inicial, que es la ruta del directorio desde el cual el usuario comenzará a navegar. Si no se proporciona una ruta, la función utiliza el directorio actual de trabajo, que se obtiene con os.getcwd().

Dentro de la función, se inicia un bucle infinito (while True), que seguirá ejecutándose hasta que el usuario decida salir.

Al principio de cada iteración del bucle, la función imprime el directorio_actual para que el usuario sepa en qué parte del sistema de archivos se encuentra.

Luego, la función lista todos los archivos y carpetas en el directorio_actual, imprimiéndolos con un índice numérico que los usuarios pueden usar para hacer su selección.

Después de listar los archivos y directorios, se solicita al usuario que ingrese su selección:

Si el usuario ingresa "salir", el bucle se rompe y la función termina.
Si el usuario ingresa "volver", la función asciende un nivel en la jerarquía de directorios, usando os.path.dirname(directorio_actual) para obtener el directorio padre.
Si el usuario ingresa "cambiar", se le solicita que ingrese una nueva ruta de directorio inicial. Si la ruta proporcionada es válida y es un directorio, se actualiza directorio_actual a esta nueva ruta.
Si el usuario ingresa un número que corresponde a uno de los índices impresos, la función verificará si este índice se refiere a una carpeta dentro del directorio_actual:
Si es una carpeta, cambia directorio_actual a esa carpeta, permitiendo que la próxima iteración del bucle muestre su contenido.
Si no es una carpeta, se informa al usuario y se le pide que intente de nuevo.
Si el usuario ingresa algo que no es reconocido o no es válido, la función imprime un mensaje de error y solicita nuevamente la entrada.

Esta función es útil para scripts que requieren interacción del usuario para navegar a través de la estructura de directorios del sistema de archivos, seleccionando directorios y cambiando el contexto de trabajo según sea necesario.
