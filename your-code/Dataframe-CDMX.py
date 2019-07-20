#Librerias
import pandas as pd
import requests
from datosgobmx import client
import urllib

#Usando la funcion de client de datosgobmx
#Y usando la el metodo parse.quote_plus() de la libreria urllib podemos escribir acentos
estaciones_request = client.makeCall('sinaica',{'pageSize':5000,'date':'2018-07-18T12:00:00.000Z','state':urllib.parse.quote_plus('Ciudad de México')})

#Regresa un diccionario y lo convertimos a DataFrame 
results = pd.DataFrame(estaciones_request['results'])
cd_mx_json_r.loc[:2]


#Usando requests podemos usar las comparaciones de unicode y utf-8 para el formato en los caracteres especiales 
cd_mx = requests.get('https://api.datos.gob.mx/v2/sinaica?state=Ciudad de M%C3%A9xico&date=2018-07-18T12:00:00.000Z&pageSize=1000')
cd_mx_json=cd_mx.json()
cd_mx_json_r = pd.DataFrame(cd_mx_json['results'])
cd_mx_json_r.loc[:2]