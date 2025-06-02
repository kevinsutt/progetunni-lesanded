sisend = str(input("Sisestage üks sõna: "))

sõne = list(sisend) # eraldame tähed
i = 1 # globaalne indeks
def tagurpidi(sisend): # funktsioon, mis pöörab sõna ümber teiselt poolt
    global i
    try:
        sisend = sisend
    except(NameError, TypeError, ValueError):
        return "Antud sisend ei ole sobilik!"
    if not sisend:
        return ""
    if len(sisend.strip().split()) != 1:
        return "Sisend peab olema üks sõna"
    if any(sisend.isdigit() for sisend in sisend):
        return "Sisend ei tohi sisaldada numbreid"
    if i > len(sõne):
        return "" # kui läksime sõne lõpuni, tagasta tühi string
    else:
        täht = sõne[-i]
        i += 1
        return täht + tagurpidi(sisend)


print(tagurpidi(sisend)) # kuvame tulemust
