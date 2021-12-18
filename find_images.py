
#%% 
from bs4 import BeautifulSoup
import re
import requests


#%% 
fh = open('src/jean-michel-basquiat-paintings.html')
page = BeautifulSoup(fh, features="html.parser")

imgs = list(page.findAll('img'))
print(len(imgs))

#%%

family = ['mor', 'far', 'kat', 'sof']
print(len(family))
for member in family:
    print(member.upper())

#%%
print(imgs[0])

#%% 
urls = []
for img in imgs:
    src = img['src']
    if src.startswith('http'):
        if re.search('basq', src, re.IGNORECASE):
            print(src)
            urls.append(src)

# %%
urls[0].split('/')[-1]

# %%
for url in urls:

    # download url
    r = requests.get(url, allow_redirects=False)
    # split på / og tag sidste komponent
    fname = url.split('/')[-1]
    # overskriv fname med folder navn+filnavn
    fname = f'images/{fname}'
    print(fname)

    fh = open(fname, 'wb')
    fh.write(r.content)

    fh.close()

# %%
