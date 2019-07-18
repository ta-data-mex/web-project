import requests
import BeautifulSoup
import re

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