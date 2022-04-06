arvutustehe = input("Kas tahate lahutamist, liitmist, korrutamist või jagamist? ")
esimenearv = int(input("Palun sisestage esimene arv: "))
teinearv = int(input("Palun sisestage teine arv: "))    
kokku = 0
kokku2 = 0
kokku3 = 0
kokku4 = 0
def liida(kokku):
    kokku = esimenearv + teinearv
    return(kokku)

def lahuta(kokku2):
    kokku2 = esimenearv - teinearv
    return(kokku2)

def korruta(kokku3):
    kokku3 = esimenearv * teinearv
    return(kokku3)
   
def jaga(kokku4):
    kokku4 = esimenearv / teinearv
    return(kokku4)



if arvutustehe == "liitmist":
    print(liida(kokku))
elif arvutustehe == "lahutamist":
    print(lahuta(kokku2))
elif arvutustehe == "korrutamist":
    print(korruta(kokku3))
elif arvutustehe == "jagamist":
    print(jaga(kokku4))
