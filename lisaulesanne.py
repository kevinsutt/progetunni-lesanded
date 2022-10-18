# valmistamine
fail = open('nimekiri.txt', 'r+')
kast = []
for rida in fail:
    kast.append(rida)
uus = []
for rida in kast:
    uus.append(rida.strip())
    
# alakriipsude asendamine punktidega
i = 0
punktid = []
for rida in uus:
    punktid.append(uus[i].replace('_','.'))
    i = i + 1
# kõikide tähtede väiketähtedeks tegemine
i = 0
vaike = []
for rida in punktid:
    vaike.append(punktid[i].lower())
    i = i + 1

# numbrite eemaldamine (mitte domeenis!)
i = 0
numbrita = [] # no @
for rida in vaike:
    s = vaike[i]
    letter = "@"
    f = s.find(letter)
    i = i + 1
    splitime = s[:f]
    numbrita.append(splitime)

i = 0
numbrita2 = []
for rida in numbrita:
    danumba = ''.join([i for i in numbrita[i] if not i.isdigit()])  # no numbers
    numbrita2.append(danumba)
    i = i + 1

# no @
vaike2 = vaike
noat = []
i = 0
for rida in vaike2:
    s = vaike2[i]
    letter = "@"
    f = s.find(letter)
    i = i + 1
    splitime = s[f:]
    noat.append(splitime)

# tagasi panemine listi ette nähtud muudatustega
updated = []
i = 0
while i <= 99:
    updated.append(numbrita2[i] + noat[i])
    i = i + 1

################################################################
# 30 % 100-st on 30
 # ainult 2 gmaili, peab olema 30. Praegu on gmailide osakaal 2%
 # peab saama 28 gmaile juurde
 # ei tohi asendada e-maile mille domeen on suurem kui 5 tähte
 # leiame domeeni pikkuse @-ist kuni .-ini ja siis lahutame -2
################################################################
# emaili .*** osa
i = 0
lisand = [] 
for rida in noat:
    a = noat[i]
    letter = "."
    b = a.find(letter)
    i = i + 1
    splitime = a[b:]
    lisand.append(splitime)

# ainult email ja @ 
i = 0
email = [] # pikkuse lugemiseks -1 lengthist 
for rida in noat:
    a = noat[i]
    letter = "."
    b = a.find(letter)
    i = i + 1
    splitime = a[:b]
    email.append(splitime)
# gmailide asendamine, lisamine
lisakas = []
i = 0
counter = 2 # algeline gmailide osa arv
while i < len(email):
    pikkus = len(email[i])
    if (pikkus - 1) <= 5 and (counter <= 30):
        sona = email[i]
        sona = "@gmail.com"
        lisakas.append(sona)
        i = i + 1
        counter = counter + 1
    else:
        sona = email[i]
        lisakas.append(sona)
        i = i + 1
        continue
    
# ülesmises koodis on asendatud @gmail.com nii palju, kuni see võtab 30% osa listist
# domeenide kokku panemine
i = 0
puhas = []
while i < len(lisakas):
    sona = lisakas[i]
    if sona == "@gmail.com":
        i = i + 1
        puhas.append(sona)
    else:
        uus_sona = sona + lisand[i]
        i = i + 1
        puhas.append(uus_sona)

# domeeni liitmine tagasi nimesse
i = 0
valmistus = []
while i < len(puhas):
    liides = puhas[i]
    eesliide = numbrita2[i]
    kokku = eesliide + liides
    valmistus.append(kokku) # koik eelnev töö tulemus listis
    i = i + 1
    
print(valmistus) # lõpp tulemus prinditud

 
        
    

    
    
    



    

