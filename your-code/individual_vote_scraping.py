import requests
import BeautifulSoup
import re

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

