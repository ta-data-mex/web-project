import json
import requests
import pandas as pd
from pandas.io.json import json_normalize

url = 'https://xivapi.com/lore?string=legendary&columns=Text,Data'
key = '5e0b3550ab00450cbe87043f029655148261fee7e91f4cb484a9d0e73ee2f7f7'
data = requests.get(url, key)
data2 = data.json()
flattened_data = json_normalize(data2)
flattened_data1 = json_normalize(flattened_data.Results[0])
flattened_data1

df = pd.DataFrame(flattened_data1)
df = df.drop(['Data.Name_cn','Data.Name_en','Data.Name_kr','Data.Icon'], axis=1)

redf = df.rename(columns={"Data.GamePatchID":"Patch", "Data.ID":"ID","Data.Name":"En_Name", "Data.Name_de":"Gr_Name", "Data.Name_fr":"Fr_Name","Data.Name_ja":"Jp_Name", "Data.Url":"Url", "Text":"Lore"})

print(redf)