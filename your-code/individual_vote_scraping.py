import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

'''
El código de esta página hará lo siguiente:
- Importar csv de la home de votaciones
- Hacer requests por cada votación con un link pattern + id de votación
- Por cada content, guardar lo siguiente:
    - Nombre, partido y voto de cada diputado
- DF unificado con siguientes columnas:
    - Nombre, partido, voto, ID de votación (se repite por cada diputado de cada votación)
- exportar .csv
'''

pattern = 'https://www.camara.leg.br/presenca-comissoes/votacao-portal?reuniao=54984&itemVotacao=%s'
url = pd.read_csv('./data/votacoes_geral.csv')
ids = url['ID Votacao'].tolist()

lst_dfs = []
for i in ids:
    tmp = requests.get(pattern % i).content
    tmp_soup = BeautifulSoup(tmp, 'html')
    spans = [[l.text for l in el if l != '\n'] for el in tmp_soup.select('.partidosContainer li')]
    spans = [s for s in spans if len(s) > 0 and (s[-1] == 'Sim' or s[-1] == 'Não' or s[-1] =='Obstrução')]
    spans_df = pd.DataFrame(spans)
    spans_df['ID Votacao'] = i
    lst_dfs.append(spans_df)

votos = pd.concat(lst_dfs, axis=0, ignore_index=True)
votos.columns = ['Nome', 'Partido', 'Voto', 'ID Votacao']
votos.to_csv('./data/votos.csv', index=False)