sisend = input("Palun sisestage arvjada: ")
if ',' in sisend:
    jada = sisend.split(",")  # eemaldame tühikud, lõikame koma järgi
else:
    jada = sisend.split()  # tühikute järgi

def pikkus(jada): # vaatame, mitu liiget on listis
    if jada == []:
        return 0
    else:
        return 1 + pikkus(jada[1:])

print(pikkus(jada)) # kuvame tulemust
