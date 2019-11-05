#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64
import pandas as pd
import requests as r
import ast

print("""
 _     _            ___  _____   __ ______      _        
| |   (_)           |  \/  |\ \ / / |  _  \    | |       
| |    _  __ _  __ _| .  . | \ V /  | | | |__ _| |_ __ _ 
| |   | |/ _` |/ _` | |\/| | /   \  | | | / _` | __/ _` |
| |___| | (_| | (_| | |  | |/ /^\ \ | |/ / (_| | || (_| |
\_____/_|\__, |\__,_\_|  |_/\/   \/ |___/ \__,_|\__\__,_|
          __/ |                                          
         |___/                                    
      """)


url = "https://ligamx.net/cancha/estadisticahistorica/1/"
base64_string = b'eyJpZERpdmlzaW9uIjoiMSIsImlkVGVtcG9yYWRhIjoiNzAiLCAiaWRUb3JuZW8iOiIxIn0='

header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'} 

decoded = base64.decodebytes(base64_string)
dec = decoded.decode('UTF-8').replace("'", '"')

d = ast.literal_eval(dec)

n = int(d['idTemporada']) - 1

l = []

for i in range(11):
    for x in range(2,0,-1):
        l.append(str({'idDivision': '1', 'idTemporada': str(n), 'idTorneo': str(x)}).replace(' ', '').replace("idTorneo", " idTorneo").replace("'", '"').replace('"," ', '", "'))
    n-=1
    
encodedStrings = [str(base64.b64encode(bytes(i, 'utf-8')),'utf-8') for i in l]
urls = [(url + i) for i in encodedStrings]

dfs_list = []

def create_dfs(url):
    cont = r.get(url, headers = header).content
    t = pd.read_html(cont, attrs = {'class': 'default tbl_grals'})
    t[0].columns = t[0].columns.droplevel(level=0)
    df = t[0]
    columns=[('General','POS'),('General','Club'),('TOTAL','JJ'),('TOTAL','JG'), ('TOTAL','JE'),('TOTAL','JP'),('TOTAL','GF'),('TOTAL','GC'),('TOTAL','Dif'),('TOTAL','PTS'),
         ('LOCAL','JJ'),('LOCAL','JG'),('LOCAL','JE'),('LOCAL','JP'),('LOCAL','GF'),('LOCAL','GC'),('LOCAL','Dif'),('LOCAL','PTS'),
         ('VISITANTE','JJ'),('VISITANTE','JG'),('VISITANTE','JE'),('VISITANTE','JP'),('VISITANTE','GF'),('VISITANTE','GC'),('VISITANTE','Dif'),('VISITANTE','PTS')]
    df.columns=pd.MultiIndex.from_tuples(columns)
    dfs_list.append(df)

temporada = 2018
torneo = 2

#URL inicial insertada en input, generar DF inicial
create_dfs(url + str(base64_string))

try:
    for url in urls:
        create_dfs(url)
        print(f'[+] Temporada:{temporada}, Torneo:{torneo} --> Appended: ok!')
        torneo-=1
        if torneo == 0: 
            torneo = 2
            temporada -= 1
except ValueError as e: print(e)

with pd.ExcelWriter('Estadisticos_LigaMX.xlsx') as writer:
    dfs_list[0].to_excel(writer, sheet_name=f'Temp 2019, Torneo 1')
    for df in dfs_list:
        df.to_excel(writer, sheet_name=f'Temp {temporada}, Torneo {torneo}')
        torneo-=1
        if torneo == 0: 
            torneo = 2
            temporada -= 1
print("[+] Excel Generado!")

def sum_dfs(df_list):
    tables = []
    for table in df_list:
        table.columns = table.columns.droplevel(level=0)
        table.sort_values('Club', inplace = True)
        tables.append(table)
    return tables

sum_dfs(dfs_list)

result = pd.concat(dfs_list)

final_table = result.groupby(['Club']).sum()

final_table = final_table.drop(columns = ['POS'])

columns=[('TOTAL','JJ'),('TOTAL','JG'), ('TOTAL','JE'),('TOTAL','JP'),('TOTAL','GF'),('TOTAL','GC'),('TOTAL','Dif'),('TOTAL','PTS'),
         ('LOCAL','JJ'),('LOCAL','JG'),('LOCAL','JE'),('LOCAL','JP'),('LOCAL','GF'),('LOCAL','GC'),('LOCAL','Dif'),('LOCAL','PTS'),
         ('VISITANTE','JJ'),('VISITANTE','JG'),('VISITANTE','JE'),('VISITANTE','JP'),('VISITANTE','GF'),('VISITANTE','GC'),('VISITANTE','Dif'),('VISITANTE','PTS')]

final_table.columns=pd.MultiIndex.from_tuples(columns)

final_sorted_by_pts = final_table.sort_values([('TOTAL', 'PTS')], ascending=False)

top_ten = final_sorted_by_pts[:10]

top_total = final_sorted_by_pts.sort_values([('TOTAL', 'PTS')], ascending=False)
top_ten_total = top_total[:10]
top_ten_total = top_ten_total['TOTAL']

top_local = final_sorted_by_pts.sort_values([('LOCAL', 'PTS')], ascending=False)
top_local_ten = top_local[:10]
top_local_ten = top_local_ten['LOCAL']

top_vis = final_sorted_by_pts.sort_values([('VISITANTE', 'PTS')], ascending=False)
top_vis_ten = top_vis[:10]
top_vis_ten = top_vis_ten['VISITANTE']







