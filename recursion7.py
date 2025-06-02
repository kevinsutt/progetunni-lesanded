sõnebefore = str(input("Sisestage üks sõna: "))
vokaalid = ['a', 'e', 'i', 'o', 'u', 'ä', 'ö', 'õ', 'ü']
sõne = list(sõnebefore)  # muundame listiks
i = 0  # globaalne indeks
def konsonandid(sõnebefore): # võtame ära konsonandid ja avaldame tulemuse
    global i
    try:
        sõnebefore = sõnebefore
    except (NameError, TypeError, ValueError):
        return "Antud sisend ei ole sobilik!"
    
    if len(sõnebefore.strip().split()) != 1:
        return "Sisend peab olema üks sõna"
    
    if any(char.isdigit() for char in sõnebefore):
        return "Sisend ei tohi sisaldada numbreid"
    
    if i >= len(sõne):
        return ""  #  kui läksime sõne lõpuni, tagasta tühi string
    
    esimene = sõne[i]
    
    if esimene.lower() in vokaalid:
        i += 1
        return konsonandid(sõnebefore)
    else:
        i += 1
        return esimene + konsonandid(sõnebefore)
        
print(konsonandid(sõnebefore)) # avaldame tulemuse
