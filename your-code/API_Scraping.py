import requests
import time
from pathlib import Path

import pandas as pd

res = requests.get('http://sepomex.icalialabs.com/api/v1/zip_codes?city=tlaxcoapan')

res.json()

url = 'http://sepomex.icalialabs.com/api/v1/zip_codes?city=tlaxcoapan'
ciudades = []
for i in range(15):
    res = requests.get(url)
    ciudad = res.json()
    ciudad.keys()
    ciudades.append(ciudad['zip_codes'])   
    
df = pd.DataFrame(ciudades[0])

filename = "Código_Postal.csv"
filename = "Data/"+ filename

if not Path(filename).is_file():
    df.to_csv(filename, index=False)
    print(f"{filename} saved.")
else: 
    print('File already exists.')
        
        
print("Finished")