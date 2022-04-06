from laul import Laul
import csv

tabel = []

with open("laulud.csv", encoding="utf-8") as fail:
    csv_fail = csv.reader(fail, delimiter=";")
    for rida in csv_fail:
        tabel.append(rida)



laulud = []

for rida in tabel:
    laul = Laul(rida[1], rida[0], rida[2])
    laulud.append(laul)


kas_jatkata = True
while kas_jatkata:
    print("Tee valik, kuidas soovid laulu otsida:")
    print("1: otsing laulu pealkirja järgi")
    print("2: otsing artisti järgi")
    print("3: otsing artisti järgi")

    valik = input("Valik [1, 2, 3]: ")

    if valik == "1":
        otsitav = input("Sisesta otsitav laul (osa pealkirjast): ")
        for laul in laulud:
            if otsitav.lower() in laul.pealkiri.lower():
                laul.näita()
    elif valik == "2":
        otsitav = input("Sisesta otsitav artist (osa nimest): ")
        for laul in laulud:
            if otsitav.lower() in laul.esitaja.lower():
                laul.näita()
    elif valik == "3":
        otsitav = input("Sisesta otsitav vaatamisarv: ")
        loendur = 0
        for laul in laulud:
            if int(otsitav) < int(laul.vaatamisarv):
                if 10 > loendur:
                    loendur = loendur + 1
                    laul.näita()

    else:
        print("Valik ei olnud 1 ega 2. Game over!")
        kas_jatkata = False
    print("++++++++++++++++++++++++++++++++++++++++")
