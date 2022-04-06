from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlopen
i = 0
url = 'https://voco.ee/koolielu/toetavad-teenused/arstiabi/'
sisu = requests.get(url).text
doc = BeautifulSoup(sisu, "html.parser")
tabelid = doc.find_all('table')
tabel = tabelid[0]
tbody = tabel.tbody
read = tbody.find_all('tr')
i = 0
j = 0
vastus = urlopen("https://voco.ee/koolielu/toetavad-teenused/arstiabi/")
baidid = vastus.read()
tekst = baidid.decode()
nimed = re.findall('(>)(Ko.*)(,)', tekst)
print(nimed[0][1])
for rida in read:
        print(' - ' + rida.text.replace("\n", " "))
        i += 1
        
print("")
vastus2 = urlopen("https://voco.ee/koolielu/toetavad-teenused/arstiabi/")
baidid2 = vastus2.read()
tekst2 = baidid2.decode()
nimed2 = re.findall('()([Põ](.*))(,)', tekst2)
print(nimed2[0][1])
doc2 = BeautifulSoup(sisu, "html.parser")
tabel2 = tabelid[1]
tbodys = tabel2.tbody
reads = tbodys.find_all('tr')
for rida in reads:
        print(' - ' + rida.text.replace("\n", " "))
        i += 1
        
