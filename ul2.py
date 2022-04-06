import math
fail = open("raamatud.txt", encoding="UTF-8")
kirjandus_tabel = [] # Tühi järjend, kuhu lisame raamatud
for rida in fail:    # Iga rea jaoks failist
    raamat = []     # Kogume reas olevad raamatu pealkirja ja lehekülgede arvu järjendisse
    osad = rida.split(":") # Jupitame rea semikooloni koha pealt

    pealkiri = osad[0].strip() # Eraldame pealkirja
    leheküljed = int(osad[1].strip()) # Eraldame lehekülgede arvu

    raamat.append(pealkiri) # Lisame reas olevad raamatu pealkirja ja lehekülgede arvu järjendisse
    raamat.append(leheküljed)

    kirjandus_tabel.append(raamat) # Lisame raamatute järjendi kirjanduse tabelisse
# 1 lk = 500 sõna == 2 min jooksul
# 2h päevas
# 60lk päevas ja 30 000 sõna
a = []
i = 0
while i < len(kirjandus_tabel):
    a.append(kirjandus_tabel[i][1])
    i = i + 1
qq = []
numbrid = []
i = 0
while i < len(a):
    fff = (a[i] / 60)
    aa = math.ceil(a[i] / 60)
    i = i + 1
    qq.append(aa)
    fff = round(fff * 2)
    numbrid.append(fff)
    
i = 0
the = []
for i in range(len(kirjandus_tabel)):
    kirjandus_tabel[i][1] = qq[i]   
i = 0
while i < len(kirjandus_tabel):
    if kirjandus_tabel[i][1] > 4:
        the.append(kirjandus_tabel[i])
    i = i + 1   
i = 0
while i < len(the):
    the[i].insert(1, '-')
    the[i].insert(3, 'päeva')
    i = i + 1
i = 0
print("Raamatud, mille lugemiseks kulub rohkem kui neli päeva: ")
while i < len(the):
    print(*the[i]) 
    i = i + 1  
kak = sum(numbrid)
print("Kõigi raamatute lugemiseks kulub " + str(kak) + "h.")
fail.close()
