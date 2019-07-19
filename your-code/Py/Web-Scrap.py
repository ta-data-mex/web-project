import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

#https://na.finalfantasyxiv.com/lodestone/freecompany/9228579323923932444/member/?page=1
url = 'https://na.finalfantasyxiv.com/lodestone/freecompany/9228579323923932444/member/?page=1'
html = requests.get(url).content
links = BeautifulSoup(html, 'html5lib')

player = links.find_all('p',{'class' : 'entry__name'})
world = links.find_all('p',{'class' : 'entry__world'})
rank = links.find_all('ul',{"class" : "entry__freecompany__info"})

playerstr = str(player)
worldstr = str(world)
rankstr = str(rank)

cleanp = re.sub(r'<(.*?)>','', playerstr).split(',')
cleanp = [i.replace('[','').replace(']','') for i in cleanp]

cleanw = re.sub(r'<(.*?)>','', worldstr).replace('\xa0','').split(',')
cleanw = [i.replace('[','').replace(']','') for i in cleanw]

cleanr = re.sub(r'<(.*?)>','', rankstr)
cleanr = re.sub(r'\d','',cleanr).split(',')
cleanr = [i.replace('[','').replace(']','') for i in cleanr]

p_df = pd.DataFrame(cleanp)
w_df = pd.DataFrame(cleanw)
r_df = pd.DataFrame(cleanr)

fc_df = pd.concat([p_df, w_df], axis=1)
fc_df2 = pd.concat([fc_df, r_df], axis=1)
columns = ['Player_Name','World/Server','Rank']
fc_df2.columns = columns
fc_df2 = fc_df2.iloc[:50]
fc_df2 = fc_df2.iloc[:50]

print(fc_df2)