a = input("Sisetage üks numbriline väärtus: ")
b = input("Sisestage üks numbriline väärtus: ")

def euclid(a, b): # eukleidese algoritm 
    try:
        a = float(a)
    except (NameError, TypeError, ValueError):
        return "A väärtus peab olema arvuline"
    try:
        b = float(b)
    except (NameError, TypeError, ValueError):
        return "B väärtus peab olema arvuline"
    if b == 0:
        return a
    else:
        return euclid(b, a % b)

print(euclid(a,b))
