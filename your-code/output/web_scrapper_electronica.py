from bs4 import BeautifulSoup
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import random as rd
from selenium.webdriver.chrome.options import Options

url1 = 'https://www.taloselectronics.com/collections/arduino?page=1&grid_list=grid-view'
url2 = 'https://www.taloselectronics.com/collections/arduino?page=2&grid_list=grid-view'
url3 = 'https://www.taloselectronics.com/collections/arduino?page=3&grid_list=grid-view'

path = r'C:\Program Files\ChromeDriver\chromedriver.exe'
ruta_archivo = r'..\output\articulos_electronica.csv'

def get_source(url):
    ''' Esta función toma una url y regresa el código fuente
        utilizando el driver de Chrome
    '''
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    
    driver = webdriver.Chrome(path, options=chrome_options)
    driver.get(url)

    rand_keys(driver)

    page_source = driver.page_source
    print('Extracción terminada')
    driver.quit()

    return page_source


def rand_keys(driver):
    ''' Esta función envía teclas presionadas al driver de Chrome.
        La tecla presionada es aleatoria así como el intervalo de
        tiempo entre cada acción.
    '''
    keys_list = ['END', 'HOME', 'ARROW_DOWN', 'ARROW_UP']
    time.sleep(rd.randint(1,3))

    for i in range(rd.randint(1,20)):
        ActionChains(driver).send_keys(Keys.ARROW_DOWN).perform()
        print('Presionando tecla')
        time.sleep(rd.randint(1,3))

# Generando la sopa
def give_me_soup(source):
    """ Esta función toma un listado de urls y devuelve un listado de contenidos html
        en forma de sopa.
    """
    soup = BeautifulSoup(source, 'html')
    return soup

page_to_scrap = input('Ingresa el número de la página que vamos a scrapear: 1, 2 o 3')
while page_to_scrap not in ['1','2','3']:
    page_to_scrap = input('Ese numero no es válido. 1, 2 o 3')

if page_to_scrap == '1':
    url = url1
elif page_to_scrap == '2':
    url = url2
elif page_to_scrap == '3':
    url = url3

sources = get_source(url)
soup = give_me_soup(sources)

articulo = soup.select('ul div a')

# Extrayendo el link de su tag y almacenandolo en una lista
links = [articulo[i]['href'] for i in range(len(articulo))]
links_href = []
for link in links:
    if link not in links_href:
        links_href.append(link)

# Purgando la lista de links para dejar sólo artículos
art_links = ['https://www.taloselectronics.com/'+link for link in links_href if link.startswith('/collections/arduino')]

# Entrando a cada url de los artículos de la página y extrayendo su contenido
# articles = [get_source(art_link) for art_link in art_links]
articles = []
for i,art_link in enumerate(art_links):
    print(f'obteniendo el artículo num. {i} de {art_link}\n')
    get_source(art_link)

# Obteniendo el HTML de cada artículo
art_soups = [give_me_soup(art) for art in articles]

# Extrayendo nombre y precio de cada artíciulo en una lista
articles_name = []
articles_price = []
for art_soup in art_soups:
    articulo = art_soup.select('h1')
    articulo = articulo[0].text.strip()
    articles_name.append(articulo)
    precio = art_soup.select('article span[class="money"]')
    precio = precio[1].text.strip()  
    articles_price.append(precio)

# Creando un dataframe vació con dos columnas
df = pd.DataFrame(columns=['articulo','precio'])

# Creando dos tablas con nombres y precios c/u y concatenandolos en el dataframe
articulos = pd.DataFrame(articles_name)
precios= pd.DataFrame(articles_price)
df = pd.concat([articulos, precios], axis=1)

if page_to_scrap == '1':
    # Guardar primera tabla
    df.to_csv(ruta_archivo, index=False)
    print('archivo CSV actualizado') 
    df_anterior = df
    print(f'Tabla de articulos en {url1}: \n')
    df_anterior

 
elif page_to_scrap == '2':

    df_anterior = pd.read_csv(ruta_archivo)
    nuevo_df = df_anterior
    nuevo_df = pd.concat([df])
    nuevo_df.to_csv(ruta_archivo, index=False)
    print(f'Tabla de articulos en {url1} y {url2}: \n')
    print('archivo CSV actualizado')  
    nuevo_df

else:
    df_anterior = pd.read_csv(ruta_archivo)
    nuevo_df = df_anterior
    nuevo_df = pd.concat([df])
    nuevo_df.to_csv(ruta_archivo, index=False)
    print(f'Tabla de articulos en {url1}, {url2} y {url3}: \n')
    print('archivo CSV actualizado')  
    nuevo_df