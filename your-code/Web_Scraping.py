import time
import re
import sys
import requests
from pathlib import Path

import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_page(url):
    
    #randint = np=random.randint
    
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    
    path = r'/Applications/Chrome Driver/chromedriver'
    driver = webdriver.Chrome(path, chrome_options=options)
    
    driver.get(url)
    time.sleep(5)
    
    page_source = driver.page_source
    driver.quit()
    return page_source

def airbnb_cancun(page_source):
    
        selection = BeautifulSoup(page_source, 'html')
        try: 
            title_airbnb = selection.select('span[class="_im5s6sq"]')
            price_airbnb = selection.select('div > span[class^="a8jt5op"]')
            rate_airbnb = selection.select('span[class="_10fy1f8"]')
            evaluation_airbnb = selection.select('span[class="_a7a5sx"]')
            amenity_airbnb = selection.select('div[class="_12oal24"]')
            link_airbnb = selection.select('div a[href^="/rooms"]')
        except:
            price_airbnb = selection.select('div > span[class^="a8jt5op"]')
            rate_airbnb = selection.select('span[class="_10fy1f8"]')
            evaluation_airbnb = selection.select('span[class="_a7a5sx"]')
            amenity_airbnb = selection.select('div[class="_12oal24"]')
            link_airbnb = selection.select('div a[href^="/rooms"]')
        
    
        titles_rooms = [title.get_text() for title in title_airbnb]
        prices_rooms = [price.get_text() for price in price_airbnb[2:-1]]
        rates_rooms = [rate.get_text() for rate in rate_airbnb]
        evaluations_rooms = [re.sub(r'[\xa0()]','', evaluation.get_text()) for evaluation in evaluation_airbnb]

        amenities_rooms = []
        for div in amenity_airbnb:
                amenities = div.find_all('span', class_="_3hmsj")
                amenities_rooms.append([amenity.get_text() for amenity in amenities])

        links = ['https://www.airbnb.mx' + link['href'] for link in link_airbnb]
        links_rooms = []
        for link in links:
            if link not in links_rooms:
                links_rooms.append(link)

        return [titles_rooms, prices_rooms, amenities_rooms, rates_rooms, evaluations_rooms, links_rooms]  
    
def airbnb_project():
    url ='https://www.airbnb.mx/s/Canc%C3%BAn--Mexico/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_dates%5B%5D=december&flexible_trip_dates%5B%5D=november&flexible_trip_lengths%5B%5D=weekend_trip&date_picker_type=calendar&query=Canc%C3%BAn%2C%20Mexico&place_id=ChIJ21P2rgUrTI8Ris1fYjy3Ms4&adults=2&source=structured_search_input_header&superhost=true&search_type=unknown&federated_search_session_id=5a3cd58a-7091-4f53-9815-f47f44eaee0f&pagination_search=true'
    page_source = get_page(url)
    airbnb_ = airbnb_cancun(page_source)
    
    filename = "Airbnb_Cancun.csv"
    filename = "Data/"+filename
    t = airbnb_[0]
    p = airbnb_[1]
    a = airbnb_[2]
    r = airbnb_[3]
    e = airbnb_[4]
    l = airbnb_[5]
    
    
    df = pd.DataFrame(zip(t, p, a, r, e, l), columns = ['Titles','Price','Rating','Evaluation','Amenities','Links'])
    df.head()
    if not Path(filename).is_file():
        df.to_csv(filename, index=False)
        print(f"{filename} saved.")
    else: 
        print('File already exists.')
        
        
    print("Finished")

airbnb_project()
    