# TP_N_4
## consigna
Crear tres clases en Python, que cumplan con lo siguiente:

* Una clase llamada "Nota".

 * Sus variables de instancia son:
  1. id: Un número secuencial automático
  2. texto: El texto de la nota
  3. etiquetas: una serie de palabras-clave separadas por espacios
  4. fecha_creacion: la fecha de creación de la nota

 * Además del método iniciador (__init__) debe tener un método llamado "coincide", que reciba como parámetro una cadena, y que retorne True si la cadena forma parte del texto o de las etiquetas, y False de lo contrario.

* Una clase llamada "Anotador". Su única variable de instancia es "notas", una lista de objetos Nota.
 * Sus métodos son:
  1. nueva_nota: Recibe un texto y agrega a la lista una nueva nota con ese texto.
  2. _buscar_por_id: Recibe un id, y retorna la el objeto Nota correspondiente, o None si no existiera.
  3. modificar_nota: Recibe un id y un nuevo texto, y actualiza el texto de la nota.
  4. modificar_etiquetas: Recibe un id y las nuevas etiquetas, y actualiza las etiquetas de la nota.
  5. buscar: Recibe un "filtro" (cadena de búsqueda) y retorna una lista compuesta por las notas cuyo texto o etiquetas coincidan con el filtro recibido.

* Una clase llamada Menu, que contiene una interfaz de usuario básica en línea de comandos.
