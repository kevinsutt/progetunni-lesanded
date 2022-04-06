# Failis "grupid.txt" on õpilasgrupid, kes soovivad kõik sel laupäeval mängida tennist. Igal real on grupiliikmete arv.

# Tennisehall nimega "Reketiässad" mahutab 128 mängijat ja on vaba.
# Tennisehall nimega "Tennisehundid" mahutab 192 mängijat ja on samuti vaba.
küssa = input("Faili nimi: ")
arvud = []
listt = 0
jäta = 0
leid = 0
lause = 0
rly = 0
def listimine(listt):
    fail = open(küssa, "r")
    for rida in fail:
        arvud.append(int(rida))
        
def jäta(jäta):
    daa = arvud[i]
    saa = kokku - daa
    saa = int(saa)
    if saa <= 128:
        saa = int(saa)
        lause = "ei tuleks väljakuid juurde otsida."
    elif saa <= 192:
        saa = int(saa)
        lause = "ei tuleks väljakuid juurde otsida."
    elif saa <= 320:
        saa = int(saa)
        lause = "ei tuleks väljakuid juurde otsida."
    elif saa > 193:
        saa = int(saa)
        lause = "tuleks ikka väljakuid juurde otsida."
    return lause
        

    
appendimine = listimine(listt)

kokku = sum(arvud)
length = len(arvud)
i = 0

if kokku <= 128:
    print("Kokku registreerus " + str(kokku) + " inimest" + "." + " Broneerida tuleks Reketiässad.")
    
elif kokku <= 192:
    print("Kokku registreerus " + str(kokku) + " inimest" + "." + " Broneerida tuleks Tennisehundid.")
    
elif kokku > 320:
    print("Kokku registreerus " + str(kokku) + " inimest" + "." + " Tuleb väljakuid juurde otsida.")

    
elif kokku > 193:
    print("Kokku registreerus " + str(kokku) + " inimest" + "." + " Broneerida tuleks mõlemad.")
    

while i < length:
    kus = str(print("Õpilasgrupi arvuga " + str(arvud[i]) + " väljaätmisel " + str(jäta(jäta))))
    i = i + 1
