# ALGBASS
from bs4 import BeautifulSoup
import requests

url = "https://siseveeb.voco.ee/veebivormid/restorani_menuu"

sisu = requests.get(url).text
doc = BeautifulSoup(sisu, "html.parser")
# SOE TOIT
soojadtoidud = doc.find_all("tr")
print("SOE TOIT")
for s in soojadtoidud:
    vee = s.find_all("td")
    for f in vee:
        print(f.text)
print("SUPID")
listike = []
#for soetoit in soojadtoidud:
 #   print(soetoit.contents[0].table, end="\n")
# SUPID 
soojadtoidud2 = doc.find_all("tr")[0]

for s2 in soojadtoidud2:
    vee2 = s2.find_all("p")
    for f2 in vee2:
        print(f2.text)

    
# MAGUSTOIT
print("MAGUSTOIT")
soojadtoidud3 = doc.find_all("tr")[1]

for s3 in soojadtoidud3:
    vee3 = s3.find_all("p")
    for f3 in vee3:
        print(f3.text)

# KÜLMTOIT
print("KÜLMTOIT")
soojadtoidud4 = doc.find_all("tr")[2]

for s4 in soojadtoidud4:
    vee4 = s4.find_all("p")
    for f4 in vee4:
        print(f4.text)
