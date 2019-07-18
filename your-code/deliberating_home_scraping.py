import requests
import BeautifulSoup
import re

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