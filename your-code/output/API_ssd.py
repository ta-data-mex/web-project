import requests
import pandas as pd

ruta_archivo = r'..\output\objetos_cercanos.csv'

url = 'https://ssd-api.jpl.nasa.gov/cad.api?body=all'
res = requests.get(url)
res_json = res.json()

res_json.keys()

fields = res_json['fields']
data = res_json['data']

df = pd.DataFrame(data, columns=fields)

df = df[['des','orbit_id','cd','dist','v_rel','t_sigma_f','body','h']]

columnas = ['Designacion', 'id_orbita', 'Fecha_aproximacion_cercana', 
'Distancia_au', 'Velocidad_relativa_km/s','Incertidumbre_temporal',
'Cuerpo','Mgnitud_absoluta']

df.columns = columnas

print(df.info())
print(df.head())

df.to_csv(ruta_archivo,index=False)