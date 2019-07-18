import requests
import BeautifulSoup
import re

'''
El código de esta página hará lo siguiente:
- Importar csv de la home de sesion
- Request por cada link de votación
- En cada link, encontrar lo siguiente:
    - ID de votaciones de la sesión (presentes en un dropdown menu de la página)
- DataFrame con 2 columnas:
    - Link del voto (**se repite por los IDs de votación de una misma reunión)
    - ID de votaciones
- exportar .csv
'''