
#%% 
from bs4 import BeautifulSoup
import re
import requests


# %%

# åbn en fil og lad beautifulsoup læse den og forstå html strukturen
fh = open('src/jean-michel-basquiat-paintings.html')
page = BeautifulSoup(fh, features="html.parser")

# gem alle image tags i en liste
imgs = list(page.findAll('img'))


# %%
urls = []  # en tom liste
for img in imgs:  # loop over alle image tags

    # tag src attributen ud af tag'et
    src = img['src']
    if src.startswith('http'):

        # hvis 'basq' er i src'en ...
        if re.search('basq', src, re.IGNORECASE):
            # tilføj til listen
            urls.append(src)


# %%
for url in urls:

    # download url
    r = requests.get(url, allow_redirects=False)
    # split på / og tag sidste komponent
    fname = url.split('/')[-1]
    # overskriv fname med foldernavn/filnavn
    fname = f'images/{fname}'

    # lav ny fil ('w') som skal have binært data ('b')
    fh = open(fname, 'wb')
    # save downloaded content i filen
    fh.write(r.content)

    # luk filen (fortæller operativ systemet at du er færdig)
    fh.close()
