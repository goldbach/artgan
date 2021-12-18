
#%% 
from bs4 import BeautifulSoup
import re

#%% 
page = BeautifulSoup(
    open('jean-michel-basquiat-paintings'),
    features="html.parser"
    )

#%% 
imgs = list(page.findAll('img'))
urls = []
for img in imgs:
    src = img['src']
    if src.startswith('http'):
        if re.search('basq', src, re.IGNORECASE):
            urls.append(src)
            print(src)

# %%
# %%
