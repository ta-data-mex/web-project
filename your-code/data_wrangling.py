import pandas as pd
import re

'''
El código de esta página hará lo siguiente:
- Importar archivos .csv que creamos durante scraping a pandas DataFrame
- Generar relaciones entre los DataFrames a través de IDs
- Limpiar textos y generar nuevas columnas si es necesario
- Generar variables categóricas condicionales (partidos gobierno vs oposición)
- Generar dummies para votos (sí, no, obstrucción)
- Exportar datasets listos a csv
'''

mother_df = pd.read_csv('./data/mother_page.csv')
meetings_df = pd.read_csv('./data/deliberacoes.csv')
votings_df = pd.read_csv('./data/votacoes_geral.csv')
votes_df = pd.read_csv('./data/votos.csv')

def remove(corpus):
    corpus = corpus.lower()
    corpus = re.sub(r'[\.\,\!\?\"\'\¡\¿\:]', '', corpus)
    corpus = corpus.replace('\n', '').replace('\f', '')

mother_df['Titulo'] = mother_df['Titulo'].str.lower().str.replace('\n', ' ').str.replace('\t', '')
mother_df['Data'] = mother_df['Titulo'].str.extract(r'(\d{2}\/\d{2}\/\d{4})', expand=True)
mother_df['Titulo'] = mother_df['Titulo'].str.replace(r'(\d{2}\/\d{2}\/\d{4})', '').str.strip()
mother_df['ID reuniao'] = mother_df['links'].str.extract(r'(\d+$)', expand=True)

mother_order = ['ID reuniao', 'Data', 'Titulo', 'links']
mother_df = mother_df[mother_order]
mother_df.columns = ['ID_reuniao', 'Data', 'Detalhes', 'Link_reuniao']

print(meetings_df)