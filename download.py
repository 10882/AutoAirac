import requests
import bs4
import zipfile
import os

def pars():
    req = requests.get('https://xn--80aaahf3a6ahgmiw8k.xn--p1ai/')
    req.encoding = 'utf-8'

    soup = bs4.BeautifulSoup(req.content)
    AllData = soup.findAll('tr')
    defalt = AllData[-4]
    navdata = AllData[-5]
    fmc = AllData[-18]
    defalt = defalt.find('a')
    defalt = defalt.get('href')
    navdata = navdata.find('a')
    navdata = navdata.get('href')
    fmc = fmc.find('a')
    fmc = fmc.get('href')
    return defalt, navdata, fmc

def download(Href):
    link = 'https://xn--80aaahf3a6ahgmiw8k.xn--p1ai' + Href
    req = requests.get(link)
    fle = open(Href[9:], 'wb')
    fle.write(req.content)
    fle.close

def unzip(Href):
    fle = Href[9:]
    zipfle = zipfile.ZipFile(fle)
    zipfle.extractall('')

def remove(Href):
    fle = Href[9:]
    os.system('del '+ fle)