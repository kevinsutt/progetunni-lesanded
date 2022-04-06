import sqlite3
arv = 50


count = 50
# ül 3
def näita_ridu(andmed):
    print("Päringu tulemus: ")
    arv = 50
    loendur = 0
    count = 50
    daa = ("UPDATE edetabel SET punktid = punktid + 50 WHERE eesnimi = 'Kaspar'")
    for rida in andmed:
        loendur += 1
        print(rida[2] + " " + rida[1] + " - punktid: " + str(rida[3]))
    # kui päringu vastuseks ei tulnud midagi, siis loendur jäi nulli
    # ei olnud võimalik teha kontrolli len(andmed) == 0, sest "andmed" on tegelikult kursor, kus len() ei toimi
    if loendur == 0:
        print ("Andmeid ei leitud!")
    return daa


# avame andmebaasi
ühendus = sqlite3.connect('its_andmed.db')
# loome virtuaalse käsurea ("kursor" on nagu virtuaalne käsurida, mille kaudu saab saata käske andmebaasile)
c = ühendus.cursor()
# näita kõiki ridu tabelist
c.execute("SELECT * FROM edetabel")
f = näita_ridu(c)
f = f
c.execute(f)



print("")
print("Teeme muudatuse.")
# suurenda ühe rea punktisumma ja näita uut tulemust
c.execute("UPDATE edetabel SET punktid = 1001 WHERE eesnimi = 'Kersti'")
# ül 2
c.execute("SELECT * FROM edetabel WHERE eesnimi = 'Kaspar'")
näita_ridu(c)
    
# kursor on ka ilus sulgeda
c.close()
# salvestame kõik tehtud muudatused ("commit" = salvestamine)
ühendus.commit()
# sulgeme ühenduse
ühendus.close()

