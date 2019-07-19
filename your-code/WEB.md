{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## WEB SCRAPING\n",
    "###NFL QB\n",
    "\n",
    "Lo que no logré con el API sí lo logré con el web scraping; sacar información estadistica sobre la NFL y en especifico de los QB.\n",
    "\n",
    "Encontré una pagina que se llama sports reference donde vienen estadisticas historicas de cada deporte y dentro de cada equipo, jugador o liga.\n",
    "\n",
    "Como quería buscar de QB de la nfl entre a su pagina y vi que tenian distinta informacion en cada página. Mi proposito era ver que tan distante era la estadistica del Passer Rating con las estadisitcas básicas como pass attempts, pass completions, yards, TD, o inteceptions. \n",
    "\n",
    "El passer rating toma en cunta todas estas estadisticas y con una formula : NFL Passer Rating =(((((B2/C2)-0.3)*5)+(((D2/C2)-3)*0.25)+((E2/C2)*20)+(2.375-((F2/C2)*25)))/6)*100\n",
    "\n",
    "con la siguiente información:\n",
    "    Completions in Column B\n",
    "    Attempts in Column C\n",
    "    Passing Yards in Column D\n",
    "    Touchdowns in Column E\n",
    "    Interceptions in Column F\n",
    "    \n",
    "Se supone que esta formula califica a los qb de manera completa para poder rankearlos, el problema era que un qb con solo un partido jugado, si lo hace muy bien su passer rating será muy alto y eso no lo convierte en un grande de la NFL. POr eso comparé tomé como DF base los attempts pues sólo los QB con más cantidad de attempts estarian contemplados.\n",
    "\n",
    "Cada estadistica era un scraping diferente pues estaba en una pagina diferente.\n",
    "\n",
    "El primer scraping entonces fue de la tabla de attempts en la que vienen: el jugador, los attempts, los años de su carrera y los equipos en los que jugó.\n",
    "NOTA: estos datos vienen en cada pagina, solo cambian los datos de attempts por la estadistica que se este buscando.\n",
    "\n",
    "Elimine la columna de los equipos pues no tenía mucha relevancia, y para saber cuantos años habia jugado o ha jugado cada jugador separe la columna de los años el año de inicio y el del final de su carrera o el ultimo que estuvieron acttivos y de ahi saque la cantidad de años que ha jugado.\n",
    "\n",
    "Con esos pasos hice una función que metiendo el url de la pagina de las diferentes estadisticas te devuelva el Dataframe limpio y listo para analizar.\n",
    "\n",
    "Realice este proceso con las demas estadisticas (completions, yds, td, interceptions y passer rating)\n",
    "\n",
    "Despues tuve el problema de unir los DF por el nombre pero cuando lo logre hacer me di cuenta de que no se podian ordenar los valores numericos porque no eran de tipo numerico sino objetos.\n",
    "\n",
    "Cambié los tipos de los valores y ya pude ordenar los datos por cada estadistica basica.\n",
    "\n",
    "Mis resultados fueron que en las estadisticas básicas los mismos nombres estan siempre arriba salvo por uno o dos que van cambiando, pero se mantienen muy constante y cuando revisamos el orden por passer rating vemos que por lo menos los primeros dos nombres cambian y de los 10 primeros de las estadisticas basicas se mantienen 3 en el top 10 del passer rating. \n",
    "\n",
    "El diferenciador es claro, la cantidad de juegos hacen que sea más dificil mantener unn buen passer rating mientras más attempts y juegos tengas.\n",
    "\n",
    "Es por eso que yo pienso que para saber quienes son los nombres grandes en los QB de la nfl las estadisticas basicas son la manera, en cambio el passer rating funciona más para calificar partidos individuales y no carreras.\n",
    "\n",
    "\n",
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
