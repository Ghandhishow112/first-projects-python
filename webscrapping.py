from bs4 import BeautifulSoup
from urllib.request import urlopen
def extract_files():
    html=urlopen('https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)')
    bsobj=BeautifulSoup(html, 'lxml')
    body=bsobj.find('div' , {'class' , 'mw-page-container-inner'})
    headi=bsobj.find_all('div', {'class', 'mw-heading mw-heading2','mw-heading mw-heading3'})
    title=bsobj.find('span', {'class' , 'mw-page-title-main'})
    print('these are the headers tag:')
    print(title.text)
    for head in headi:
        
    
        print(head.get_text())
    print('these are the image links:')    
    for link in bsobj.findAll('img'):
        if 'src' in link.attrs:
            
           print(link.attrs['src'])
    

extract_files()
