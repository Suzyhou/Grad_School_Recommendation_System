#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import requests


# In[8]:


def web_scrapping(school,major,degree_type,num_pages):
    DATA_DIR = './data/'
    baseurl='https://www.thegradcafe.com/survey/?per_page=40&q=&institution={}&program={}&degree={}&page={}'

    for i in range(1, int(num_pages)):
        url = baseurl.format(school,major,degree_type,i)
        r = requests.get(url)
        fname = "{data_dir}/{page}.html".format(data_dir=DATA_DIR, page=str(i))
        with open(fname, 'wb') as f:
            f.write(r.text.encode('UTF-8'))
        print("getting {0}...".format(i))

# In[ ]:




