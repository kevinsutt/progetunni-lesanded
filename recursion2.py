def auto_hind(hind, aastahulk):## funktsioon, mis leiab auto väärtuse X aasta tagant ning aluseks on Y väärtusega auto hind
    try:
        hind = float(hind)
    except (NameError, TypeError, ValueError):
        return "Hind peab olema arvuline"
    try:
        aastahulk = float(aastahulk)
    except (NameError, TypeError, ValueError):
        return "Aastahulk peab olema arvuline"
    if (hind == 0):
        return "Võimatu hind"
    elif (aastahulk == 0):
         return hind
    else:
        vahe = hind * 0.2 # väärtus kahaneb igal aastal 20% võrreldes eelmise hinnaga
        return auto_hind(round((hind := hind - vahe),2), aastahulk - 1)
