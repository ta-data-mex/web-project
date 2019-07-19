import pandas as pd
import re

'''
El código de esta página hará lo siguiente:
- Importar archivos .csv que creamos durante scraping a pandas DataFrame
- Generar relaciones entre los DataFrames a través de IDs
- Limpiar textos y generar nuevas columnas si es necesario
- Generar dummies para votos (sí, no, obstrucción)
- Exportar datasets listos a csv
'''
#Leer archivos
mother_df = pd.read_csv('./data/mother_page.csv')
meetings_df = pd.read_csv('./data/deliberacoes.csv')
votings_df = pd.read_csv('./data/votacoes_geral.csv')
votes_df = pd.read_csv('./data/votos.csv')

#Limpiar texto de mother_df y expandir columnas necesarias
mother_df['Titulo'] = mother_df['Titulo'].str.lower().str.replace('\n', ' ').str.replace('\t', '')
mother_df['Data'] = mother_df['Titulo'].str.extract(r'(\d{2}\/\d{2}\/\d{4})', expand=True)
mother_df['Titulo'] = mother_df['Titulo'].str.replace(r'(\d{2}\/\d{2}\/\d{4})', '').str.strip()
mother_df['ID reuniao'] = mother_df['links'].str.extract(r'(\d+$)', expand=True)

#Limpiar texto de meetings_df y expandir columnas necesarias
meetings_df['Tema'] = meetings_df['Tema'].str.lower().str.strip().str.replace('\n', ' ').str.replace('\t', '').str.replace('\s{2}', '', regex=True)
text_meetings = meetings_df['Tema'].str.extract(r'tema:(.+)local:(.+)início:(.+)término:(.+)situação:(.+)', expand=True)
text_meetings.columns = ['Tema', 'Local', 'Inicio', 'Termino', 'Situacao']
meetings_df = meetings_df.drop('Tema', axis=1)
meetings_df = pd.concat([meetings_df, text_meetings], axis=1)

#Concatenar meetings_df a mother_df
mother_df = pd.concat([mother_df, meetings_df], axis=1)

#Cambiar orden y nombre de columnas del nuevo mother_df
mother_order = ['ID reuniao', 'Data', 'Tema', 'Local', 'Inicio', 'Termino', 'Situacao', 'Titulo', 'links', 'Links Votacoes']
mother_df = mother_df[mother_order]
mother_df.columns = ['ID reuniao', 'Data', 'Tema', 'Local', 'Inicio', 'Termino', 'Situacao', 'Detalhes', 'Link Reuniao', 'Link Votacoes']

#Exportar a csv
mother_df.to_csv('./data/mother_df_clean.csv', index=False)

#Cambiar orden de las columnas de votings_order
votings_order = ['ID Votacao', 'ID Reuniao', 'Titulo Votacao']
votings_df = votings_df[votings_order]

#Exportar a csv
votings_df.to_csv('./data/votacoes_clean.csv', index=False)

#Limpiar texto, generar dummies, cambiar order y exportar
votes_df['Partido'] = votes_df['Partido'].str.strip('(').str.strip(')')
votes_dummies = pd.get_dummies(votes_df['Voto'])
votes_df = pd.concat([votes_df, votes_dummies], axis=1)
votes_order = ['ID Votacao', 'Nome', 'Partido', 'Voto', 'Sim', 'Não', 'Obstrução']
votes_df = votes_df[votes_order]

votes_df.to_csv('./data/votos_clean.csv', index=False)



