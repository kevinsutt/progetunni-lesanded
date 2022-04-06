
hinnete_tabel = [['eesti keel', 5, 4, 3, 4, 4, 3, 4, 4],
                 ['matemaatika', 4, 4, 5, 5, 4, 5, 5, 4, 5],
                 ['keemia', 4, 3, 3, 2, 3, 4],
                 ['kirjandus', 5, 5, 5, 4, 5, 5, 4],
                 ['bioloogia', 4, 5, 4, 4, 3, 5, 5, 5]]


# keskmist arvutad nii, et liidad kõik kokku ja jagad, i arvuga.
# i arv on nii palju numbreid listis
# näiteks: 5,5,5 == 5 + 5 + 5 = 15 / 3 = 5

# Leidke iga tund keskmine

eestikeel = hinnete_tabel[0]
matemaatika = hinnete_tabel[1]
keemia = hinnete_tabel[2]
kirjandus = hinnete_tabel[3]
bioloogia = hinnete_tabel[4]

def keskminehinne(tund):
    del tund[0]
    hinded = tund 
    summa = 0
    i = 0
    for hind in hinded:
        summa = summa + tund[i]
        i = i + 1
    vastus = summa / (len(tund) )
    return float(vastus)

print(eestikeel[0] + "e " + "keskmine hinne on " + str(round(keskminehinne(eestikeel), 2)))

print(matemaatika[0]  + " keskmine hinne on " + str(round(keskminehinne(matemaatika), 2)))

print(keemia[0] + " keskmine hinne on " + str(round(keskminehinne(keemia), 2)))

print(kirjandus[0] + "e " + "keskmine hinne on " + str(round(keskminehinne(kirjandus), 2)))

print(bioloogia[0] + " keskmine hinne on " + str(round(keskminehinne(bioloogia), 2)))
    
    
