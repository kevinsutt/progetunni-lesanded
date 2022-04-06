import datetime
from datetime import date
isikukood = input("Sisestage oma isikukood: ")
# 37602128822 76 on aasta 02 on kuu 12 on päev
# tahame võtta osad kus on kuupäev
isikukood.splitlines()
aasta = int(isikukood[1:3])
kuu = int(isikukood[3:5])
päev = int(isikukood[5:7])
# päev on päev see ei muutu
# kuu ei muutu, jääb kuuks
# aasta muutub, võib olla 20 sajand kui ka 21

print("Aasta on " + str(aasta) + ", kuupäev on " + str(päev) + "." + str(kuu) + ".")
todays_date = date.today()
praegune = todays_date
praegu_aasta = str(todays_date.year)[2:4]
#print(praegu_aasta)

a = (int(aasta))
b = int(praegu_aasta)

if a>b: 
    age = b-a+100
else: 
    age = b-a
    
print(age)
