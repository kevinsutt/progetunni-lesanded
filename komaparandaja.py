fail = open("vigane.txt", encoding="UTF-8")
def asendus(lause):
    lause = lause.replace(" aga ", ", aga ")
    lause = lause.replace(" et ", ", et ")
    lause = lause.replace(" kui ", ", kui ")
    return lause

for rida in fail:
    print(asendus(rida.strip()))



with open("vigane.txt") as f:
    with open("parandatud.txt", "a") as f1:
        for rida in f:
            f1.write(asendus(rida))
           
           
#par_fail = open("parandatud.txt", "w", encoding="UTF-8")
#par_fail.write()

   
   
fail.close()
