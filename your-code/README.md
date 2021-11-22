# Web Scrapping Project

Para este proyecto, extraje la información de la pagina de bookmarks.review en el apartado de best rewiewed con el fin de obtener la siguiente información:
- Título del libro
- Autor
- Editorial 
- Fecha de publicacion
- Calificación universal del libro
- Numero de reseñas
- Categoria
- Ligas para el total de reseñas

Para extraer las ligas de los libros del apartado best reviews use selenium, ya que, al tratarse de una página dinámica, solicite qué bajara la pagina
en un número aleatorio entre 3 y 5 veces con selenium. 
Posteriormente, hice uso de BeautifulSoup para extraer el contenido html de las paginas de los libros y después definí una función para seleccionar los 
datos descritos en el listado anterior. Finalmente, use pandas para guardarlos en una base de datos. 

En cuanto a obstaculos del proyecto, me fue complicado hacer la función, ya que obtenia los datos que pedía, pero me los regresaba en forma de lista, debido 
a que usaba una list comprehension para poder limpiar el texto. Lo solucioné, al pedir que me regresara el primer elemento de la lista- que a fin de cuentas
era el único elemento-, y así pudiera regresarlo como el objeto que yo quería

# API Project

Para este proyecto seleccioné RapidAPI para explorar la página International Movie Database (IMDb). La documentación para el API indica varios endpoints
para expoloración de películas, series de TV, etc. con base a actores o con base a los títutlos de las películas. 

En particular quise explorar las ganancias generadas por la pelicula del "Señor de los Anillos: El Retorno del Rey" y que las ganancias las describiera 
por país. Para lograr este objetivo tuve que buscar primero el ID del título, generando un query para el nombre de la pelicula con ayuda de un diccionario.
Posteriormente explore las llaves de la información obtenida por la petición y escogi aquellas que me dieran como resultado las ganancias.
Finalmente, use pandas para almacenarlso en una base de datos.

Los obstaculos que me encontré con este proyecto fue entender que es lo que queria buscar con la información que me estaban dando, ya que todo estaba almacenado 
en diccionarios. Asi que basicamente fue ir expolorando la llave, para ver que era lo que necesitaba y asi hacer la limpieza de la información. 
Por otro lado, batalle para generar la base de datos con pandas, ya que me salía la columna con la información que queria pero comprimida en un diccionario, 
asi que tuve que razonar como hacer uso del método json_normalize para que me regresara lo que requería. 
