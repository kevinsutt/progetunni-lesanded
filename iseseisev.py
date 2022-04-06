küsimus = input("Mis on teie esimene nimi? ")
küsimus2 = input("Mis on teie teine nimi? ")
küsimus3 = int(input("Mis on teie isikukood? "))
küsimus4 = input("Mis koolis käite? ")
class Õppija:
    kool = küsimus4
    isikukood = küsimus3
    def kusõpib():
        return "Õpib koolis " + õppija1.kool
    def __init__(self, eesnimi, perekonnanimi, isikukood):
        self.eesnimi = eesnimi
        self.perekonnanimi = perekonnanimi
        self.isikukood = isikukood   
    def __str__(self):
        return "Õppija nimi: "+ self.eesnimi +" " + self.perekonnanimi + ".\n" + Õppija.kusõpib() + ".\n" + Õppija.koodike() + ".\n" + self.sugu()
    def koodike():
        return "Õppija isikukood on " + str(õppija1.isikukood)
    def sugu(self):
        if self.isikukood//10000000000%2 == 1:
            return "Õppija on mees"
        else:
            return "Õppija on naine"
        
õppija1 = Õppija(küsimus, küsimus2 , küsimus3)

print(õppija1)
