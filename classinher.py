# harjutus päriluse kohta
# ülemklass
class Auto:
    vedu = "nelikvedu"
    käigukast = "manuaal"
    
    
# alamklass
class Audi(Auto):
    bränd = "Audi"
    värv = "must"
    hind = "3000 eurot"
    kütus = "bensiin"
    
a = Audi()
    
print("See on minu " + str(a.bränd) + ", loogiliselt " + str(a.vedu) + ".")
print("Auto on " + str(a.värv) + "a" + " värvi.")
print("Käigukast on ikka " + str(a.käigukast) + ".")
print("Auto maksis umbes " + str(a.hind) + ".")
print("Kütuseks on ikka " + str(a.kütus) + ".")
