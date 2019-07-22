def grafica_delitos():
    #Nota la base tenia mas de 800 000 registros y pesaba casi 700 megas por lo que solo pude ocupar 10 000 para el proyecto
    import json
    import requests
    import feedparser
    import pymysql
    from sqlalchemy import create_engine
    import pandas as pd
    from pandas.io.json import json_normalize
    import numpy as np
    import random

    users_columns = pd.read_csv('CIPGJ_ordenado_limpio.csv')

    users_columns.sort_values(by='mes_hechos', ascending=True)

    mes=users_columns.groupby('mes_hechos').size().sort_values(ascending=False).head(10)

    users_columns.groupby('fiscalia').size().sort_values(ascending=True).head(10)

    data = users_columns.groupby('delito').size()#.sort_values(ascending=False)
    data1=dict(data)

    Delitosxmes = None
    for m, v in dict(mes).items():
        Delitos = users_columns[(users_columns['mes_hechos']==m)]
        Delitosxmes = pd.concat([Delitosxmes, pd.DataFrame(Delitos.groupby('delito').size())[0]], sort=False, axis=1)
        Delitosxmes = Delitosxmes.rename(columns={0:m})

    nulos = Delitosxmes.isnull().sum()
    Delitosxmes[Delitosxmes.columns] = Delitosxmes[Delitosxmes.columns].fillna(0)
    Delitosxmes = Delitosxmes[['Enero','Febrero','Marzo','Abril','Mayo','Agosto','Septiembre','Octubre','Noviembre','Diciembre']]

    Delitosxmes.loc[['ABANDONO DE PERSONA'], :]
    incidencia = pd.DataFrame.transpose(Delitosxmes.loc[['ABANDONO DE PERSONA'], :])
    incidencia2 = pd.DataFrame.transpose(Delitosxmes)

    dict_columns = {k+1:v for k, v in enumerate(incidencia2.columns)}
    print('ID Delito', '\t', 'Delito\n')
    for k,v in dict_columns.items():
        print(k, '\t\t', v)

    import matplotlib.pyplot as plt
    incidencia2 = pd.DataFrame.transpose(Delitosxmes)

    deli=[]
    i=1
    while 0<i and i<177:
        try:
            print(f'Ingresa el ID Delito \ndebe ser un numero entre 1 y {len(dict_columns)} \nque deses agregar a la grafica 2018')
            i=int(input('O un numero negativo para ver la grafica\n'))
        except:
            print("ingresa un numero entre 1 y ", len(dict_columns))
            i=1
            continue
        if 0<i and i<177:
            deli.append(dict_columns[i])

    #Las gráficas apreceran automáticamente incrustadas en el notebook
    #%matplotlib inline

    # Definir los datos eje x, eje y
    #incidencia = pd.DataFrame.transpose(Delitosxmes.loc[['ABANDONO DE PERSONA'], :])
    incidencia = incidencia2[deli]

    horas = list(range(len(incidencia)))

    # gráfico
    # Configurar las caracteristicas del grafico
    i=[-1]
    def suma():
        i[0]=i[0]+1
        return i[0]

    plt.figure(figsize=(20,9))
    for h in range(len(deli)):
        plt.plot(horas, incidencia[deli[h]], label = deli[h], linewidth = 4, color = (random.random(), random.random(), random.random()))
    plt.axhline(y=np.mean(incidencia.mean()), linewidth=1, color='r')
    #Definir nombres de ejes y titulo
    plt.xlabel('Ene                             Feb                             Mar                             Abl                             '
               'May                             Ags                                 Sep                                Oct                             '
               'Nov                             Dic')
    plt.ylabel('No de delitos')
    plt.title(f'comparatido de {len(deli)} delitos en 2018')
    #Mostrar leyenda, cuadricula y figura
    plt.legend()
    plt.minorticks_on()
    plt.grid(b=True, which='major', color='#666666', linestyle='-')
    plt.grid(b=True, which='minor', color='black', linestyle='-', alpha=0.2)
    plt.show()

pase ='1'
while pase == '1':
    grafica_delitos()
    pase = input("Si desea volver a graficar ingrese 1\nDe lo contrario presione cualquier tecla y luego enter\n")
