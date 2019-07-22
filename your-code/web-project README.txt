Process for extracting data:

    -Load the webpage containing the data.
    -Locate the data within the page and extract it.
    -Organise the data into a dataframe
    -Export the data into an csv file 
    -Clean, Manipulate and Filter the csv file. 

Load the webpage containing the data: 1) create a variable called ‘headers’ and assign it a string that will tell the website that we are a browser, and not a scraping tool. 2) assign the address that we want to scrape to a variable called ‘page’. 3) use the requests library to grab the code of the page and assign it to ‘pageTree’. 3) parse the website code into html. 

---------------------------------------------------------------------------------------------------------
Valor de Mercado (todas las posiciones y grupos de edad de la liga): 
https://www.transfermarkt.es/liga-mx-clausura/marktwerte/wettbewerb/MEX1/pos//detailpos/0/altersklasse/alle/plus/1
*mismo URL para las 4 páginas (100 jugadores). 

Menores de 23 años: 
https://www.transfermarkt.es/liga-mx-clausura/marktwerte/wettbewerb/MEX1/plus/1/galerie/0?pos=&detailpos=&altersklasse=u23
*mismo URL para las 4 páginas (100 jugadores). 

Menores de 21 años: 
https://www.transfermarkt.es/liga-mx-clausura/marktwerte/wettbewerb/MEX1/plus/1/galerie/0?pos=&detailpos=&altersklasse=u21
*mismo URL para las 2 páginas (42 jugadores). 

Cuando juntemos estos DataFrames, muchos jugadores se van a repetir (incluso habrá jugadores que aparezcan tres veces), habrá que eliminar a los duplicados en el dataframe final.  

Grupos de edad: Todos, u19, u20, u23, 23-30, o30, o32 y o34

¿Qué queremos de este primer paso? Un DataFrame con los siguientes datos de los jugadores: índice(ránking), nombre, posición, nacionalidad, edad, club, valor más alto de carrera y valor de mercado. Es decir, básicamente todas las columnas de la tabla EXCEPTO 'última revisión'. 


