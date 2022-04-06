# importime vajalikke asju
from urllib.request import urlopen
import re

# ÜL : Tahame leida e-mailid ja lisada need andmed juurde nimedele, mille vahel on semikoolon
# leiame nimed
a = []
b = []
vastus = urlopen("https://kpkoda.ee/kohtutaiturid/kohtutaiturid-kontakt/")
baidid = vastus.read()
tekst = baidid.decode()
nimed = re.findall('(<h3 class="kohtu__item__title">)(.*)(</h3>)', tekst)
for nimi in nimed:
    a.append(nimi[1])
  


# leiame e-mailid
postid = re.findall('(<a href="mailto:)(.*)(">)', tekst)

for post in postid:
    b.append(post[1])


# teeme lause
for i in range(len(a)):
    print(a[i] + ";" + b[i])
