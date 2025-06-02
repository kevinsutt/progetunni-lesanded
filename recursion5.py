sisend = input("Sisestage palun tundide arv: ")
inimene = float(1)
def inimesed(sisend, inimene): # leiame üles mitu inimest teab kuulujuttu
    try:
        sisend = float(sisend)
    except (NameError, TypeError, ValueError):
        return "Sisend peab olema arvuline ning positiivne"
    if sisend < 0:
        return "Sisend peab olema positiivne"
    elif sisend == 0:
        return inimene
    else:
       return inimesed(sisend - 1, inimene + 3)

print(inimesed(sisend, inimene)) # kuvame tulemust

