import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

'''
El código de esta página hará lo siguiente:
- hacer request a 1 url de la cámara de diputados de Brasil referente a un proyecto de emenda constitucional (url_madre)
- Del contenido de la url, queremos obtener una tabla con 3 columnas:
    a) Título de la reunión
    b) Resumen de la reunión
    c) Link de la página de la reunión
- Buscaremos solamente los links que contengan el siguiente texto "Reunião Deliberativa" | "Sessão Deliberativa"
- Transformar tabla en DF y guardarla como .csv 
'''

url_madre = 'https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2192459'
PEC6 = requests.get(url_madre).content
PEC6_soup = BeautifulSoup(PEC6, 'html5lib')

# titulo_reunion = []
# resumen_reunion = []
link_reunion = PEC6_soup.find_all('a', {'href':re.compile('evento-legislativo')})
link_reunion = [item['href'] for item in link_reunion]
reuniones_df = pd.DataFrame(link_reunion)
reuniones_df.to_csv('./data/mother_page.csv', index=False)