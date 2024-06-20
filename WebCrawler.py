#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
from collections import Counter
url = 'https://www.poornima.org/'  
response = requests.get(url)
web_content = response.text
soup = BeautifulSoup(web_content, 'html.parser')
links = soup.find_all('a', href=True)
hrefs = [link['href'] for link in links]
href_counter = Counter(hrefs)
ranked_hrefs = href_counter.most_common()
for href, frequency in ranked_hrefs:
    print(f'Link: {href}, Frequency: {frequency}')

