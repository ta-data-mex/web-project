## El Chapo y Narcos Mexicanos
'Decidí obtener infromación de uno de los temas de más trascendencia en la última semana: la sentencia de Joaquín "El Chapo" Guzmán. Ya que obtuve mis KEYs de acceso a Twiiter, quise recabar las reacciones en esta red social. Además, al ser uno de los capos más importantes, decidí reflejar en una tabla el estatus de los capos mexicanos.'

## 1. API Twitter
'Al obtener mis KEYs decidí utilizar el método de api.search en la librería tweempy. Sin emabargo, encontré varias limitaciones para filtrar los tweets y a parte limpiar la información posteriormente. Así que investigué una forma de facilitarlo: tweepy.Cursor.
Con la misma librería pude filtrar los tweets por palabras, tweets o retweets, fecha, número total de tweets o número total de tweets por importancia.'

'De esta forma, no me devolvía un objeto html o json, sino que pude seleccionar e iterar sobre los tweets de una manera más sencilla. Únicamente, tuve que seleccionar mi variable y asignar la información que quería, una opción de la librería Tweepy. Después, sólo tuve que crear mi data frame y asignar los nombres que quería para las columnas.'

'Finalmente, exporté el data frame a csv.'

NOTA: No agrego mis keys por seguridad.
      Agruegué un wait_on_rate_limit en la Autorización para que cuando rebasara los límites de requests, simplemente esperara hasta que pasara el tiempo límite.

## 2. Web Scrapping
'Obtener información sobre los capos más importantes del narcotráfico no es tan sencillo. La mayoría de las bases de datos ya las otorgan en archivos csv o excel (INEGI y ONU). Por ello accedí a Wikipedia para obtener una tabla con tales datos y que puediera cumplir el objetivo de hacer Web Scrapping.'

'El scrapping fue mayormente sencillo. Realicé el request a la url y embellecí el resultado con bs4. Posteriormente, inspeccioné la página para seleccionar la clase correcta que contenía la tabla.'

'Después, tuve que iterar tres veces sobre el resultado. Primero para encontrar todas la filas (tr) y luego dos veces para acceder al texto dentro de esas filas en html.'

'Para crear la tabla, asigné dos variables a las posiciones que contenían la información y las columnas. A partir de ellas, creé el data frame y finalmente el csv.'


## 3. Pipeline 
'Tuve varios problemas al intetar crear el pipeline para ambos casos. Así que lo dejé en una función para cada uno. Ese proceso no fue tan cmplicado, pues fue utilizar el mismo método anterior, pero ahora agregando una variale a la función, la cual al ser llamda con una valor definido corriera. En el caso de la función para la API de Twitter, se podría utilizar con cualquier palabra y filtro que uno quisiera. En cambio, en wikipedia no se podría el Web Scrapping con calquier página, pues necesitaría tener una tabla forzosamente.'


##
'En general, avancé mucho en la simplificación del código, aunque aún tengo varios temas que estudiar para poder escribir un data pipeline de manera eficiente.'