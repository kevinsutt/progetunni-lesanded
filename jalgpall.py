fail = open("jalgpall.txt")
vana = [] # failist tehtud list
ilma = [] # ilma newlineita
eesti = [] # ainult eesti
# listide vahel liikumine ja muutmine
with open('jalgpall.txt', 'r') as f:
    for rida in f:
        vana.append(rida)

for element in vana:
    ilma.append(element.strip())

for element in ilma:
    if "Estonia" in element:
        changed = element.replace(":", " ")
        eesti.append(changed)
    else:
        continue
# lugeme kõik eesti võidud
# peame lugema scorei
# listid ja variaablid
i = 0
l = 0
a = 0
eesti_esimene = []
eesti_teine = []
muu_esimene = []
muu_teine = []
# whilei loop kus leitakse numbrid üles
while i < 2114:
    listike = eesti[i].split()
    if 'Estonia' in listike[l]:
        f = eesti[i].split()            # f[-2] on eelviimane arv ja f[-1] on viimane arv
        num1 = f[-1]
        num2 = f[-2]
        eesti_esimene.append(num2)
        muu_teine.append(num1)
        i = i + 1
    else:
        f = eesti[i].split()
        num1 = f[-1]
        num2 = f[-2]
        eesti_teine.append(num1)
        muu_esimene.append(num2)
        i = i + 1
# skoori lugemine on selle all
q = 0
p = 0
p2 = 0
p3 = 0
p4 = 0
# convertime strings listi intergeri listiks
int_eesti_esimene = [int(x) for x in eesti_esimene]
int_muu_teine = [int(x) for x in muu_teine]
int_eesti_teine = [int(x) for x in eesti_teine]
int_muu_esimene = [int(x) for x in muu_esimene]

# arvutused
for i in int_eesti_esimene:
    if int_eesti_esimene[q] > int_muu_teine[q]:
        p = p + 1
        q = q +1
    else:
        q = q + 1
q = 0
for i in int_muu_teine:
    if int_muu_teine[q] > int_eesti_esimene[q]:
        p2 = p2 + 1
        q = q + 1
    else:
        q = q + 1  
q = 0
for i in int_eesti_teine:
    if int_eesti_teine[q] > int_muu_esimene[q]:
        p3 = p3 + 1
        q = q + 1
    else:
        q = q + 1   
q = 0
for i in int_muu_esimene:
    if int_muu_esimene[q] > int_eesti_teine[q]:
        p4 = p4 + 1
        q = q + 1
    else:
        q = q + 1

x = (p + p2 + p3 + p4)
print("Vastus on " + str(x)) # vastus
