#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests as r
import pandas as pd
import numpy as np
import re

url = "https://www.transfermarkt.com/liga-mx-apertura/startseite/wettbewerb/MEXA/plus/?saison_id=2010"

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

response = r.get(url, headers=header)

cont = r.get(url, headers = header).text
t = pd.read_html(cont, attrs = {'class': 'items'})[0]

t.drop(columns=['Club', 'Club.1', 'Players playing abroad', 'name.1', 'Total MV', 'ø MV'], inplace= True)
t.rename({'name':'Club', 'Squad':'Edad Promedio Jugador', 'ø age':'Jugadores Extranjeros', 'Total market value':'Valor Promedio de Jugador(€)', 'ø market value':'Valor Equipo(€)'}, axis = 1, inplace = True)

t.index = np.arange(1,len(t)+1)
df_list = []

for i in range(12, 20):
    cont = r.get(f"https://www.transfermarkt.com/liga-mx-apertura/startseite/wettbewerb/MEXA/plus/?saison_id=20{i}", headers = header).content
    t = pd.read_html(cont, attrs = {'class': 'items'})[0]
    t.drop(columns=['Club', 'Club.1', 'Players playing abroad', 'name.1', 'Total MV', 'ø MV'], inplace= True)
    t.rename({'name':'Club', 'Squad':'Edad Promedio Jugador', 'ø age':'Jugadores Extranjeros', 'Total market value':'Valor Promedio de Jugador(€)', 'ø market value':'Valor Equipo(€)'}, axis = 1, inplace = True)
    t.index = np.arange(1,len(t)+1)
    df_list.append(t)
    print(f'Temporada 20{i} Done!')

with pd.ExcelWriter('Valores_Equipos_LigaMX.xlsx') as writer:
    temp = 2012
    for df in df_list:
        df.to_excel(writer, sheet_name=f'Temp {temp}')
        temp += 1
        
print("[+] Excel Generado!")

def sum_dfs(df_list):
    tables = []
    for table in df_list:
        table.sort_values('Club', inplace = True)
        tables.append(table)
        #result = pd.concat(tables).groupby(['Club']).sum()          
    return tables

sum_dfs(df_list)

result = pd.concat(df_list)

def clean_euros(x):
    if "mil. €" in x: return int(re.sub(" mil. €",'000000', x).replace(',',''))
    if "K €" in x: return int(re.sub(' K €','000', x))

df_list[-1] = df_list[-1].dropna()

for df in df_list:
    df['Jugadores Extranjeros'] = df['Jugadores Extranjeros'].apply(lambda x: int(x))
    df['Valor Promedio de Jugador(€)'] = df['Valor Promedio de Jugador(€)'].apply(clean_euros)
    df['Valor Equipo(€)'] = df['Valor Equipo(€)'].apply(clean_euros)
    df['Edad Promedio Jugador'] = df['Edad Promedio Jugador'].apply(lambda x: x/80)

result = pd.concat(df_list)

final_table = result.groupby(['Club']).sum()

top_valuable_teams = final_table.sort_values('Valor Equipo(€)', ascending=False)

top_jug_extr = final_table.sort_values('Jugadores Extranjeros', ascending=False)

top_edad = final_table.sort_values('Edad Promedio Jugador', ascending=False)

top_edad_joven = final_table.sort_values('Edad Promedio Jugador', ascending=True)
top_edad_joven = top_edad_joven[top_edad_joven['Edad Promedio Jugador'] > 19]
top_valor_jug_prom = final_table.sort_values('Valor Promedio de Jugador(€)', ascending=False)









