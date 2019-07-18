import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

'''
El código de esta página hará lo siguiente:
- Importar csv de la home de sesion
- Request por cada link de votación
- En cada link, encontrar lo siguiente:
    - Titulo votacion
    - ID de votaciones de la sesión (presentes en un dropdown menu de la página)
- DataFrame con 2 columnas:
    - Link del voto (**se repite por los IDs de votación de una misma reunión)
    - ID de votaciones
- exportar .csv
'''

url = pd.read_csv('./data/deliberacoes.csv')
url_patterns = url['Links Votacoes'].tolist()

buscar_titulo = 'option'  #text
buscar_detalles = 'option'  #value

def spider_text_id(lista_url, criterio_txt, criterio_value):
    lst_criteriot = []
    lst_criteriov = []
    lst_reuniones = []
    for el in lista_url:
        try:
            tmp = requests.get(el).content
            tmp_soup = BeautifulSoup(tmp, 'html5lib')
            lst_criteriot.append([at.text for at in tmp_soup.select(criterio_txt)])
            lst_criteriov.append([at['value'] for at in tmp_soup.select(criterio_value)])
            lst_reuniones.append([el.split('=')[-1] for at in tmp_soup.select(criterio_value)])
        except:
            continue

    print(len(lst_criteriov))
    print(len(lst_criteriot))
    return [[lst_criteriot[i],lst_criteriov[i],lst_reuniones[i]] for i in range(0,len(lst_criteriov))]

lista_votacoes = spider_text_id(url_patterns, buscar_titulo, buscar_detalles)
lista_votacoes = [[el[0][i].strip(), el[1][i], el[2][i]] for el in lista_votacoes for i in range(len(el[0]))]
votacoes_df = pd.DataFrame(lista_votacoes)
votacoes_df.columns = ['Titulo Votacao', 'ID Votacao', 'ID Reuniao']
votacoes_df.to_csv('./data/votacoes_geral.csv', index=False)