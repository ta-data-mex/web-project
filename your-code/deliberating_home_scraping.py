import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time

'''
El código de esta página hará lo siguiente:
- importar el csv de la mother_page;
- Hacer request a cada uno de los links presentes en el DF de la mother_page
- En cada uno de los links, recoger la siguiente información:
    - Detalles de la sesión
    - Link para página de votos (si hay)
- Unificar DataFrame que contenga las siguientes columnas:
    - Link de mother_page (posteriormente lo transformaremos en ID identificador)
    - Detalles de sesión (una sola columna, posteriormente lo limpiaremos)
    - Link para página de votos.
- Exportar a CSV.
'''

url = pd.read_csv('./data/mother_page.csv')
url_patterns = url['links'].tolist()

buscar_detalles = '.detalhes-sessao'
buscar_link_votos = ['a', {'href':re.compile('votacao-portal')}]

def spider_2columns(lista_url, criterio_txt, criterio_link):
    lst_criteriot = []
    lst_criteriol = []
    for el in lista_url:
        tmp = requests.get(f'https:{el}').content
        tmp_soup = BeautifulSoup(tmp, 'html5lib')
        lst_criteriot.append([at.text for at in tmp_soup.select(criterio_txt)][0])
        lst_criteriol.append(([at['href'] for at in tmp_soup.find_all(criterio_link[0], criterio_link[1])]or[''])[0])
    return [lst_criteriot, lst_criteriol]

lista_deliberacoes = spider_2columns(url_patterns, buscar_detalles, buscar_link_votos)
deliberacoes_df = pd.DataFrame(lista_deliberacoes).transpose()
deliberacoes_df.columns = ['Tema', 'Links Votacoes']
deliberacoes_df.to_csv('./data/deliberacoes.csv', index=False)