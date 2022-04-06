x = input("nimi:  ")
try:
    y = int(input("lubatud kiirus (km/h) : "))
except Exception as viga:
    print("Sisestati mingisugune tekst, mitte arv")
    print(str(viga))
    exit()
try:
    z = int(input("tegelik kiirus (km/h) : "))
except Exception as viga1:
    print("Sisestati mingisugune tekst, mitte arv")
    print(str(viga1))
    exit()
   
trahv= (z - y) * 3
if trahv < 0:
    print("Trahvi ei tule!")
    exit()
trahv = min(190, trahv)
trahv= round(trahv)
lause2= ", kiiruse ületamise eest on teie trahv " + str( trahv) + " eurot."
lause= str(x) + (lause2)
print(lause)
