#!/usr/bin/env python
# coding: utf-8

# # Proyecto API_WEB

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd
from lxml import html
from lxml.html import fromstring


# ## ¿Cuántas hectáreas de manglares existen en America?

# In[2]:


url = 'https://www.fao.org/3/j1533e/j1533e02.htm'


# In[3]:


response = requests.get(url)
html = response.content
soup = BeautifulSoup(html,'lxml')


# In[4]:


table = pd.read_html(html)
df = table[5]


# In[5]:


df.drop(index=df.index[0], axis=0, inplace=True)


# In[6]:


df = df.rename(columns=df.iloc[0])


# In[7]:


df.drop(index=df.index[0], axis=0, inplace=True)
df1 = df.dropna(how='all', axis=1)
df1


# In[ ]:





# ## API Digimon 

# In[8]:


url = 'https://digimon-api.vercel.app/api/digimon'


# In[9]:


select_pokemon = '/name/agumon'
to_search = url+select_pokemon
to_search


# In[10]:


res = requests.get(to_search)


# In[11]:


res_json = res.json()
res_json


# In[12]:


imagen = res_json[0]['img']


# In[13]:


from IPython.display import Image


# In[14]:


imagen = res_json[0]['img']
display(Image(url=imagen))


# In[ ]:




